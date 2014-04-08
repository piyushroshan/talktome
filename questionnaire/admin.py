from questionnaire.models import *
from django.contrib import admin
class QuesAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content' , 'ques_bank') 
    search_fields = ('subject', 'ques_bank')
    fields = ('ques_type','subject', 'ques_bank', 'content', 'score')
admin.site.register(Ques,QuesAdmin)
admin.site.register(Response)
admin.site.register(UserProfile)
admin.site.register(Option)
admin.site.register(QuestionBank)
admin.site.register(Subject)
admin.site.register(UserScore)
admin.site.register(Answer)