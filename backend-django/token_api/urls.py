from django.urls import path
from .views.login_view import Login

urlpatterns = [
    path('login', Login.as_view(), name='login'),
]
