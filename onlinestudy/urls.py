from django.conf.urls import patterns, url
from onlinestudy import views

urlpatterns = patterns('',
    url(r'^onlinestudy$', views.onlinestudy, name='onlinestudy'),
)