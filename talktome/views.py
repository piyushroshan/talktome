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
    login_var=False
    user_name=pass_word=''
    if request.POST:

        user_name = request.POST['username']
        print "username is" 
        print user_name
        pass_word = request.POST['password']
        print "passsword is"
        print pass_word
        u=UserProfile.objects.all()
        print u
        for e in u:
            temp=e.user.username
            u_percent = lcs(user_name,temp)
            if u_percent == 100 :
                percent = lcs(pass_word,e.pwd)
                print "password matching is"
                print percent
                if e.blind:
                    print "percentage matching is"
                    print percent
                    if percent >= 60 :
                        user = authenticate(username=temp, password=e.pwd)
                        if user is not None:
                            if user.is_active:
                                login_var=True
                                login(request, user)
                                return HttpResponseRedirect('/')
                    else:
                        return render_to_response('registration/login.html', {'message':"Invalid username or password."}, RequestContext(request))
                else:
                    if percent == 100:
                        user = authenticate(username=user_name, password=pass_word)
                        if user is not None:
                            if user.is_active:
                                login_var=True
                                login(request, user)
                                return HttpResponseRedirect('/')
	return render_to_response('registration/login.html', {'message':"Invalid username or password."}, RequestContext(request)) 

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    print result
    len_result=len(result)
    len_b=len(b)
    percent=(len_result*1.0/len_b)*100
    return percent