from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    # register
    path('register/', views.RegisterView.as_view(), name='register'),
    path('rule/', views.RuleView.as_view(), name='rule')
]
