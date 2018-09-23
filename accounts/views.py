# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

class SignUpView(FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('')

