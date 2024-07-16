from django.shortcuts import render
from django.views.generic import TemplateView
#import django.TemplateView

class page(TemplateView):
    template_name = "hello.html"