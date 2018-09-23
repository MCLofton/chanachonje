from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
#@login_required(login_url='/accounts/login/')
class HomeView(LoginRequiredMixin,TemplateView):
    login_url="/accounts/login/"
    redirect_field_name='redirect_to'
    template_name="index.html"


