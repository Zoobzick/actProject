from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ActCreateView(TemplateView):
    template_name = "act/act_create.html"


class ActListView(TemplateView):
    template_name = "act/act_list.html"