from questionnaire.models import UserProfile, Ques, Option, Response, Subject, QuestionBank
from django.contrib import admin
 
admin.site.register(Ques)
admin.site.register(Response)
admin.site.register(UserProfile)
admin.site.register(Option)
admin.site.register(QuestionBank)
admin.site.register(Subject)