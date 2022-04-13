from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('question/<int:i>', views.question, name='question'),
    path('tag/<int:i>', views.tag, name='tag'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('ask/', views.ask, name='ask'),
]