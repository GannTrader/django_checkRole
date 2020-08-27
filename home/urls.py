from django.urls import path
from .import views

urlpatterns = [
	path('register/', views.registerUser),
	path('login/', views.loginUser),
	path('getRegister/', views.getRegister, name = 'getRegister'),
	path('getLogin/', views.getLogin, name = 'getLogin'),
	path('level1/', views.level1),
	path('level2/', views.level2)
]