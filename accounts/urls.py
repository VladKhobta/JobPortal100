from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('employee_register/', views.employee_register.as_view(), name='employee_register'),
    path('employer_register/', views.employer_register.as_view(), name='employer_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
