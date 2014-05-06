from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	blind = models.NullBooleanField()
	#dob = models.DateField();
	#gender = models.CharField(max_length = 1)
	#blind = models.BooleanField(default= True)
	pwd = models.CharField(max_length = 256, blank=True)
	def __unicode__(self):
		return u'%s %s' % (self.user.first_name,self.user.last_name)
		
class Subject(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField(blank=True)
	def __unicode__(self):
		return self.name

class QuestionBank(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	def __unicode__(self):
		return self.name

class Ques(models.Model):
	content = models.TextField()
	ques_type = models.CharField(max_length = 1 , default= 'A')
	score = models.PositiveSmallIntegerField(max_length = 1 , default= 1)
	ques_bank = models.ForeignKey(QuestionBank)
	subject = models.ForeignKey(Subject)
	def __unicode__(self):
		return u'%s %d %s %s %s' % (self.ques_type, self.score, self.ques_bank, self.subject,  self.content)

class Option(models.Model): 
	content = models.TextField()
	question = models.ForeignKey(Ques)
	def __unicode__(self):
		return u'%s' % (self.content)

class Answer(models.Model):
	question=models.ForeignKey(Ques)
	option=models.ForeignKey(Option)

class Response(models.Model):
	user = models.ForeignKey(User)
	response = models.ForeignKey(Option) 
	question = models.ForeignKey(Ques) 
	def __unicode__(self):
		return u'%s %s %s' % (self.user, self.question, self.response)

class UserScore(models.Model):
	user = models.ForeignKey(User)
	ques_bank = models.ForeignKey(QuestionBank)
	score = models.PositiveSmallIntegerField()
