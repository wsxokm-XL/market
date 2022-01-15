from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # home
    path('home/', views.HomeView.as_view(), name='home'),
]
