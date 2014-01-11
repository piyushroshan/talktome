from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	dob = models.DateField();
	gender = models.CharField(max_length = 1)
	def __unicode__(self):
		return u'%s %s' % (self.user.first_name,self.user.last_name)

class Subject(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField()
	def __unicode__(self):
		return self.name

class QuestionBank(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	def __unicode__(self):
		return self.name

class Ques(models.Model):
	content = models.TextField()
	ques_type = models.CharField(max_length = 255)
	answer = models.PositiveSmallIntegerField(max_length = 1)
	score = models.PositiveSmallIntegerField(max_length = 1)
	def __unicode__(self):
		return u'%s %d %d %s' % (self.ques_type, self.answer, self.score, self.content)

class Option(models.Model): 
	content = models.TextField()
	index = models.PositiveSmallIntegerField(max_length = 1)
	ques_id = models.ForeignKey(Ques)
	def __unicode__(self):
		return u'%s %d %s' % (self.
			ques_id, self.index, self.content)

class Response(models.Model):
	user = models.ForeignKey(UserProfile)
	response = models.PositiveSmallIntegerField(max_length = 1)
	score = models.PositiveSmallIntegerField(max_length = 1)
	ques_id = models.ForeignKey('Ques') 
	def __unicode__(self):
		return u'%s %s %d %d' % (self.user, self.ques_id, self.response, self.score)

class Sub_qb_ques(models.Model):
	sub_id = models.ForeignKey(Subject)
	qb_id=models.ForeignKey(QuestionBank)
	ques_id=models.ForeignKey(Ques)
	def __unicode__(self):
		return u'%s %s %s' % (self.sub_id, self.qb_id, self.ques_id)

class Ques_opt(models.Model):
	ques_id=models.ForeignKey(Ques)
	opt_id=models.ForeignKey(Option)