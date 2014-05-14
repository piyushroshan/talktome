# Create your views here.
from django.http import *
from django.shortcuts import render
from questionnaire.models import *
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import random

@login_required
def subjects(request):
	subject_list = Subject.objects.all()
	context ={'subject_list' : subject_list}
	return render(request, 'questionnaire/subjects.html' , context)

@login_required
def mcq(request,subject_id):
	res=Response.objects.filter(user__username=request.user).delete()
	user=request.user
	subject = Subject.objects.get(pk=subject_id)
	qb_list=Sub_Qb.objects.filter(subject__name=subject)
	print qb_list
	qb=random.choice(qb_list)
	request.session['qb_name']=qb.ques_bank
	print "random quesbank genrated is"
	print qb.ques_bank
	ques_list = Ques.objects.filter(subject__id=subject_id,ques_bank__name=qb.ques_bank)
	question = ques_list[0]
	option = Option.objects.filter(question__id=question.id)
	try:
		user_score = UserScore.objects.get(user=user, ques_bank__name=qb.ques_bank)
	except (UserScore.DoesNotExist):
		user_score = UserScore(user=user, ques_bank=qb.ques_bank, score=0)
	user_score.score=0;
	user_score.save()
	context = {'subject_name':subject.name,'question':question,'opt_list':option,'qb':qb.ques_bank,'q_counter':1}
	response=render(request,'questionnaire/mcq.html',context)
	response.set_cookie('quesno', 0)
	return  response

@login_required
def showdetails(request):
	user=request.user
	qb_name = request.session.get('qb_name')
	print "machaak"
	print qb_name
	res=Response.objects.filter(user=user, question__ques_bank__name=qb_name)
	ans=Answer.objects.filter(question__ques_bank__name=qb_name)
	context={'ans_list':ans,'res_list':res}
	response=render(request,'questionnaire/showdetails.html',context)
	return response

@login_required
def instructions(request,subject_id):
	context={"subject_id":subject_id}
	response=render(request,'questionnaire/instructions.html',context)
	return response

def index(request):
	return render_to_response('questionnaire/index.html')
@login_required
def quit(request):
	user=request.user
	return render_to_response('questionnaire/quit.html')

def speech(request):
	return render_to_response('questionnaire/speech.html')


