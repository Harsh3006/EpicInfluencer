from django.urls import path
from campaigns import views 
 
urlpatterns = [
    path('home', views.home, name='home'),
    path('settings/personal', views.personal, name='personal'),
    path('settings/accounts', views.accounts, name='accounts'),
    path('settings/change-password', views.change_password, name='change-password')
]