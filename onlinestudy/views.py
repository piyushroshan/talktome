# Create your views here.
from django.http import *
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def onlinestudy(request):
	return render_to_response('onlinestudy/onlinestudy.html')