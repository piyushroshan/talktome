from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.conf.urls.defaults import patterns, include
from dajaxice.core import dajaxice_autodiscover, dajaxice_config 
from django.conf import settings
from talktome.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration.backends.default.views import RegistrationView
from django.views.generic.simple import direct_to_template
dajaxice_autodiscover()
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


# These urls are mapping to different views in views.py file.
urlpatterns = patterns('',
	 # Home page of talktome
#	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	(r'^questionnaire/',include('questionnaire.urls')),
	(r'^onlinestudy/',include('onlinestudy.urls')),
	# Serve static content. This line is important to serve the static content i.e the css,javascript files.
	url(r'^register/$', register, name='register'),
	(r'^accounts/', include('registration.backends.default.urls')),
	(r'^$', direct_to_template, 
            { 'template': 'index.html' }, 'index'), 
	(r'^logout/$', logout_page),
	(r'^login/$', login_user),
	#This mapping is important for incorporating Django's Admin module in our project. If removed Admin module won't work.
	(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/', include(admin.site.urls)),
    (r'^password_reset/', include('password_reset.urls')),
	
	# This line imports Dajaxice settings in our project, Important for AJAX functionality in our project. If removed AJAX functionality won't work.
    #oldstyle
    #(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    #newstyle
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
		
)

urlpatterns += staticfiles_urlpatterns()
