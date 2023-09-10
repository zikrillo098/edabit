from .views import ClientRegistration, LoginView
from django.urls import path
from django.contrib.auth.views import LogoutView

app_name = 'client'

urlpatterns = [
    path('register/', ClientRegistration.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login')
]
