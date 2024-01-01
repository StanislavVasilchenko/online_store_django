from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, VerificationTemplateView, PasswordRecoveryView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', VerificationTemplateView.as_view(), name='verify'),
    path('pass_recovery/', PasswordRecoveryView.as_view(), name='pass_recovery'),
    path('user_profile/', UserUpdateView.as_view(), name='user_profile'),
]
