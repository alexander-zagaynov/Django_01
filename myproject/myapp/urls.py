from django.urls import path
from . import views

urlpatterns = [
 path('главная/', views.index, name='index'),
 path('', views.about, name='about'),
 path('alexander/', views.data, name='data')
]
