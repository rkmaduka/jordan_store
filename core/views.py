from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
     template_name = "home.html"

class RequestCreateView(CreateView):
    model = Request
    template_name = "request/request_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('home')


# Create your views here.
