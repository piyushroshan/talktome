from django.conf.urls import patterns, url
from onlinestudy import views

urlpatterns = patterns('',
    url(r'^subjects$', views.subjects, name='subjects'),
    url(r'^(?P<subject_id>\d+)/$',views.topics, name='topics'),
    url(r'^topic/(?P<topic_id>\d+)/$',views.content, name='content'),
)