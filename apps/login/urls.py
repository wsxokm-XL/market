from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    # login
    path('login/', views.LoginView.as_view(), name='login'),
]