# Create your views here.
from django.http import *
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from onlinestudy.models import *

def subjects(request):
	subject_list = Subject.objects.all()
	context ={'subject_list' : subject_list}
	return render(request, 'onlinestudy/subjects.html' , context)

def topics(request,subject_id):
	topic_list= Topic.objects.filter(subject__id=subject_id)
	print topic_list
	context ={'topic_list' : topic_list, 'subject_id':subject_id}
	return render(request, 'onlinestudy/topics.html',context)
def content(request,topic_id):
	material= Material.objects.filter(topic__id=topic_id)
	for m in material:
		context ={'topic_content' : m.upFile.read()}
	return render(request, 'onlinestudy/content.html',context)