# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def login(request):
    """Function to login existing User"""
    #Create LoginForm object
    #Check if method is GET or POST
    #get cleaned data from form
    #auntheticate the user and raise exceptions if any.
    #redirect user to dashboard profile page.
    return render(request,'login.html',{'form':form})

def logout(request):
    #TODO
    pass

def register(request):
    #create RegistrationForm object
    #pass it to template
    #Get submitted data
    #Verify validity of data
    #Create new user object in database
    #Redirect user to login page on success
    #else reload register.html
    pass
def dashboard(request):
    #TODO
    pass

def profile(request):
    #TODO
    pass

def edit_profile(request):
    #TODO
    pass
