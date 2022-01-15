from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('office_register/', views.officeRegister, name="office_register"),
    path('office_login/', views.officeLogin, name="office_login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('applicant/<str:pk>/', views.applicant, name="applicant"),

    path('office_account/', views.officeAccount, name="office_account"),

    path('booking/<str:pk>/', views.booking, name="booking"),
    path('edit_booking/<str:pk>/', views.editBooking, name="edit_booking"),
    path('delete_booking/<str:pk>/', views.deleteBooking, name="delete_booking"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('password_reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    
    path('office_feedback/', views.officeFeedback, name="office_feedback"),
]