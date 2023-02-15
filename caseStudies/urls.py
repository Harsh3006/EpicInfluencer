from django.urls import path
from caseStudies import views
from caseStudies.views import caseView

urlpatterns = [
    path('home', caseView.as_view(),  name="case-studies-home"),
    path('story', views.story, name='story')
]
