from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Hero

# Create your views here.
class index(ListView):
  template_name = 'index.html'

  def get_queryset(self):
    return Hero.objects.all()