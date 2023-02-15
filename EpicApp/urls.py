from django.urls import path
from EpicApp import views
urlpatterns=[
    path('', views.index, name="index"),
    path('influencers', views.influencers , name='influencers'),
    path('consumers', views.consumers, name='consumers'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('about', views.about, name="about"),
    path('demo-request', views.demo_request, name='demo-request'),
    path('legal-notice', views.legal_notice, name='legal-notice'),
    path('terms', views.terms, name='terms')
]