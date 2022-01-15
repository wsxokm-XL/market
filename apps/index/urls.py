from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    # index
    path('index/', views.IndexView.as_view(), name='index'),
]
