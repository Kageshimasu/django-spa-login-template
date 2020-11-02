from django.urls import path

from .views.login_view import LoginView
from .views.create_account_view import CreateAccountView
from .views.jwt_auth_view import JwtAuthView


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('createAccount', CreateAccountView.as_view(), name='createAccount'),
    path('jwtAuth', JwtAuthView.as_view(), name='jwtAuth')
]
