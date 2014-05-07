# Create your views here.
from django.http import *
from django.shortcuts import render
from questionnaire.models import *
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def subjects(request):
	subject_list = Subject.objects.all()
	context ={'subject_list' : subject_list}
	return render(request, 'questionnaire/subjects.html' , context)

@login_required
def mcq(request,subject_id):
	user=request.user
	subject = Subject.objects.get(pk=subject_id)
	#ques_bank = QuestionBank.objects.filter(subject__id=subject_id)
	#slogan = Slogan.objects.order_by('?')[0].slogan
	ques_list = Ques.objects.filter(subject__id=subject_id,ques_bank__name='GK1')
	qb="GKE1"
	question = ques_list[0]
	option = Option.objects.filter(question__id=question.id)
	try:
		user_score = UserScore.objects.get(user=user, ques_bank__name='GK1')
	except (UserScore.DoesNotExist):
		user_score = UserScore(user=user, ques_bank__name='GK1', score=0)
	user_score.score=0;
	user_score.save()
	context = {'subject_name':subject.name,'question':question,'opt_list':option,'qb':qb}
	response=render(request,'questionnaire/mcq.html',context)
	response.set_cookie('quesno', 0)
	return  response

def index(request):
	return render_to_response('questionnaire/index.html')

def speech(request):
	return render_to_response('questionnaire/speech.html')


