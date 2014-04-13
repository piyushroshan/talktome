from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from questionnaire.models import *
from questionnaire.forms import *
from django.contrib.auth.forms import UserCreationForm 
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.http import *
from django.shortcuts import render
from questionnaire.models import *
from django.shortcuts import render_to_response,redirect

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

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'blind' in request.POST:
                profile.blind = request.POST['blind']

            if 'pwd' in request.POST:
                profile.pwd = request.POST['pwd']
            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'registration/registration_form.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def login_user(request):
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		print "passsword is" 
		print username
		username.replace(" ", "")
		password = request.POST['password']
		print "passsword is"
		print password
		password.replace(" ", "")
		print password
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
	return render_to_response('registration/login.html', context_instance=RequestContext(request)) 