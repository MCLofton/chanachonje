from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
#@login_required(login_url='/accounts/login/')
class HomeView(TemplateView):
    template_name="index.html"


