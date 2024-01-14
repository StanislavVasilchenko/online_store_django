import random

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    """Класс для отображения страницы регистрации пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify')

    def form_valid(self, form):
        """Создает ключ для верификации пользователя и отправлюет его на указанный email"""
        verify_key = ''.join([str(random.randint(0, 9)) for i in range(12)])
        new_user = form.save()
        new_user.verified_key = verify_key
        new_user.is_active = False
        new_user.save()
        send_mail(
            subject='Пароль для верификации',
            message=f'Ссылка для верификации - {verify_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        print(new_user.email)
        print(f'Ваш ключ - {verify_key}')
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для отображения страници изменения профиля пользователя"""
    model = User
    template_name = 'users/user_form.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:products')

    def get_object(self, queryset=None):
        """Возвращает залогиненного пользователя"""
        return self.request.user


class VerificationTemplateView(TemplateView):
    """Класс для отображения страници верификации пользователя"""
    template_name = 'users/verify.html'

    @staticmethod
    def post(request):
        """Метод проверки ключа пользователя"""
        ver_code = request.POST.get('verify_key')
        user_code = User.objects.filter(verified_key=ver_code).first()

        if user_code is not None and user_code.verified_key == ver_code:
            user_code.is_active = True
            user_code.save()
            return redirect('users:login')
        return render(request, 'users/verify_err.html')


class PasswordRecoveryView(LoginRequiredMixin, TemplateView):
    """Класс для отобрадения страницы смены пароля пользователя"""
    template_name = 'users/pass_recovery.html'

    @staticmethod
    def post(request):
        """Проверяет есть пользователь с email в БД и отправляет письмо с новым паролем на указанный email"""
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user is not None and user.email == email:
            new_password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
            send_mail(
                subject='Запрос на смену пароля',
                message=f'Ваш новый пароль - {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            user.set_password(new_password)
            user.save()
            return redirect('users:login')
        return redirect('users:pass_recovery')
