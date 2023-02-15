from django.shortcuts import render
from caseStudies.models import case_studies
from django.views.generic import ListView, DetailView

class caseView(ListView):
    model = case_studies
    template_name = 'caseStudies/case-studies-home.html'

def story(request):
   return render(request , 'caseStudies/customerStory.html')