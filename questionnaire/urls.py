from django.conf.urls import patterns, url
from questionnaire import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^subjects$', views.subjects, name='subjects'),
    url(r'^(?P<subject_id>\d+)/$',views.mcq, name='mcq'),
)