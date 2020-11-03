from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.create_account_view import CreateAccountView
from .views.helloworld_view import HelloWorldView

urlpatterns = [
    path('createAccount', CreateAccountView.as_view(), name='createAccount'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello', HelloWorldView.as_view(), name='hello'),
]
