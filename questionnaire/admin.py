from questionnaire.models import *
from questionnaire.forms import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
admin.site.register(UserProfile)
class QuesAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content' , 'ques_bank') 
    search_fields = ('subject', 'ques_bank')
    fields = ('ques_type','subject', 'ques_bank', 'content', 'score')
admin.site.register(Ques,QuesAdmin)
admin.site.register(Response)
admin.site.register(Option)
admin.site.register(QuestionBank)
admin.site.register(Subject)
admin.site.register(UserScore)
admin.site.register(Answer)