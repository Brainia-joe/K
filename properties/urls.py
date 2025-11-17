from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.submit_contact, name='submit_contact'),
    path('book/', views.submit_booking, name='submit_booking'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),  
    path('profile/', views.user_profile, name='user_profile'),  
    path('reset-password/', views.reset_password_request, name='reset_password_request'), 
    path('reset-password/<str:token>/', views.reset_password_confirm, name='reset_password_confirm'), 
]