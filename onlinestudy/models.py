from django.db import models
# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length = 255)
	def __unicode__(self):
		return self.name

class Topic(models.Model):
	name = models.CharField(max_length=255)
	subject=models.ForeignKey(Subject)
	def __unicode__(self):
		return u'%s %s' %(self.name, self.subject)

def only_filename(instance, filename):
    return filename

class Material(models.Model):
	upFile = models.FileField(upload_to=only_filename)
	topic = models.ForeignKey(Topic)
	subject = models.ForeignKey(Subject)
	def __unicode__(self):
		return u'%s %s' % (self.topic, self.subject)
