# Create your views here.
from django.http import *
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from onlinestudy.models import *
import re
import cgi
re_string = re.compile(r'(?P<htmlchars>[<&>])|(?P<space>^[ \t]+)|(?P<lineend>\r\n|\r|\n)|(?P<protocal>(^|\s)((http|ftp)://.*?))(\s|$)', re.S|re.M|re.I)
def plaintext2html(text, tabstop=4):
    def do_sub(m):
        c = m.groupdict()
        if c['htmlchars']:
            return cgi.escape(c['htmlchars'])
        if c['lineend']:
            return '<br>'
        elif c['space']:
            t = m.group().replace('\t', '&nbsp;'*tabstop)
            t = t.replace(' ', '&nbsp;')
            return t
        elif c['space'] == '\t':
            return ' '*tabstop;
        else:
            url = m.group('protocal')
            if url.startswith(' '):
                prefix = ' '
                url = url[1:]
            else:
                prefix = ''
            last = m.groups()[-1]
            if last in ['\n', '\r', '\r\n']:
                last = '<br>'
            return '%s<a href="%s">%s</a>%s' % (prefix, url, url, last)
    return re.sub(re_string, do_sub, text)

def subjects(request):
	subject_list = Subject.objects.all()
	context ={'subject_list' : subject_list}
	return render(request, 'onlinestudy/subjects.html' , context)

def topics(request,subject_id):
	topic_list= Topic.objects.filter(subject__id=subject_id)
	print topic_list
	context ={'topic_list' : topic_list, 'subject_id':subject_id}
	return render(request, 'onlinestudy/topics.html',context)
def content(request,topic_id):
	material= Material.objects.filter(topic__id=topic_id)
	topic=Topic.objects.get(id=topic_id)
	print topic
	for m in material:
		res = plaintext2html(m.upFile.read())
		print res
		context ={'topic_content' : res,'topic': topic}
	return render(request, 'onlinestudy/content.html',context)