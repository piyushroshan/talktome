from django.contrib.auth import logout
from django.contrib.auth.models import User
from questionnaire.models import *
from django.contrib.auth.forms import UserCreationForm 
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from datetime import datetime
from django.core.validators import email_re

#========================================================================================================================================================================================================== 
 
# RMS homepage view
def main_page(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/questionnaire/')        #checks if the user is logged in or not, If logged in then redirect him to his welcome page.
	else: 
		return render_to_response('index.html')        # if not logged in show him the home page of RMS





#logout page view 		
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

#==========================================================================================================================================================================================================		


@login_required	
def help(request):
     return render_to_response('portal/faqs.html',
                              context_instance=RequestContext(request))



#==========================================================================================================================================================================================================	
#==========================================================================================================================================================================================================

@login_required	
#profile
def profile(request):
	return render_to_response('questionnaire/profile.html',
                      context_instance=RequestContext(request))





#==========================================================================================================================================================================================================

#RMS new user registration view	
def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/questionnaire/')
	else:
		if request.method =='POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
				user.is_active = False
				user.save()

				profile=UserProfile.objects.create(user_id=user.id, designation='STU', user_type='STU' , contact_no='0000000000')
				profile.save()
				return HttpResponseRedirect('/login/') # Redirect after POST
		else:
			form = UserCreationForm() # An unbound form

		return render_to_response('registration/registration.html', {
			'form': form,
			},context_instance=RequestContext(request))