from django.urls import path

from polls import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('index', views.index, name='index')
]