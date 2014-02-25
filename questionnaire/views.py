# Create your views here.
from django.shortcuts import render
from questionnaire.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	subject_list = Subject.objects.all()
	context ={'subject_list' : subject_list}
	return render(request, 'questionnaire/index.html' , context)

@login_required
def mcq(request,subject_id):
	subject = Subject.objects.get(pk=subject_id)
	#ques_bank = QuestionBank.objects.filter(subject__id=subject_id)
	#slogan = Slogan.objects.order_by('?')[0].slogan
	ques_list = Ques.objects.filter(subject__id=subject_id,ques_bank__name='QBU1')
	qb="QBU1"
	question = ques_list[0]
	option = Option.objects.filter(question__id=question.id)
	context = {'subject_name':subject.name,'question':question,'opt_list':option,'qb':qb}
	response=render(request,'questionnaire/mcq.html',context)
	response.set_cookie('quesno', 0)
	return  response

def indexx(request):
	return render_to_response('questionnaire/indexx.html')



