# Create your views here.
from django.shortcuts import render
from questionnaire.models import *

def index(request):
	subject_list = Subject.objects.all()
	context ={'subject_list' : subject_list}
	return render(request, 'questionnaire/index.html' , context)

def mcq(request,subject_id):
	subject=Subject.objects.get(pk=subject_id)
	ques=Ques.objects.filter(subject__id=subject_id,ques_bank__name='QBU1')
	for ques_l in ques:
		option=Option.objects.filter(question__id=ques_l.id)
	context={'subject_name':subject.name,'ques_list':ques,'opt_list':option}
	return render(request,'questionnaire/mcq.html',context)

