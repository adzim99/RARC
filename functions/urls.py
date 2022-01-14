from django.urls import path

from django.contrib.auth import views as auth_views
from django.conf.urls import include

from . import views

urlpatterns = [
    path('applicant_register/', views.applicantRegister, name="applicant_register"),
    path('applicant_login/', views.applicantLogin, name="applicant_login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('applicant/<str:pk>/', views.applicant, name="applicant"),

    path('applicant_account/', views.applicantAccount, name="applicant_account"),

    path('booking/<str:pk>/', views.booking, name="booking"),
    path('edit_booking/<str:pk>/', views.editBooking, name="edit_booking"),
    path('delete_booking/<str:pk>/', views.deleteBooking, name="delete_booking"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('password_reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    
    path('feedback/', views.feedback, name="feedback"),
]