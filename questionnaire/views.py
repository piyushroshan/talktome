# Create your views here.
from django.shortcuts import render
from questionnaire.models import Subject

def index(request):
	subject_list = Subject.objects.all()
	context ={'subject_list' : subject_list}
	return render(request, 'questionnaire/index.html' , context)