import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify')

    def form_valid(self, form):
        verify_key = ''.join([str(random.randint(0, 9)) for i in range(12)])
        print(len(verify_key))
        new_user = form.save()
        new_user.verified_key = verify_key
        new_user.is_active = False
        new_user.save()
        send_mail(
            subject='Пароль для верификации',
            message=f'Ссылка для верификации - http://localhost:8000/verify/{verify_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        print(new_user.email)
        print(f'Ваш ключ - {verify_key}')
        return super().form_valid(form)


class VerificationTemplateView(TemplateView):
    template_name = 'users/verify.html'

    @staticmethod
    def post(request):
        ver_code = request.POST.get('verify_key')
        user_code = User.objects.filter(verified_key=ver_code).first()

        if user_code is not None and user_code.verified_key == ver_code:
            user_code.is_active = True
            user_code.save()
            return redirect('users:login')
        return render(request, 'users/verify_err.html')
