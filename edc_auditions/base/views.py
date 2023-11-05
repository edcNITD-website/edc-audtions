from django.shortcuts import render, redirect
from django.contrib.auth.decorators import(
    login_required,
)

from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
import pendulum, datetime

# Create your views here.

def home(request):
    context  = {}
    return render(request, 'pages/home.html', context)
