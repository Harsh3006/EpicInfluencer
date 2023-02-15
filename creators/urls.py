from django.urls import path
from creators import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),   
    path('logout', views.logout, name='logout'),
    path('send-email', views.send_activation_email, name='send-activation-email'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('resest-password', views.RequestPasswordReset, name='reset-password'),
    path('request-reset-password/<uidb64>/<token>', views.RenderResetPasswordTemplate, name='request-reset-password'),
]