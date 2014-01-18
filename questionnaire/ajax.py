from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.models import User
from dajax.core import Dajax
from datetime import datetime
from datetime import time
from datetime import date
from questionnaire.models import *
import jsonpickle
from django.db.models import Q
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

@dajaxice_register()
def response_user(request,question,option):
    dajax = Dajax()
    user = request.user
    question = Ques.objects.get(pk=question)
    option = Option.objects.get(pk=option)
    ques_bank = question.ques_bank
    answer = Answer.objects.get(question=question)
    response = Response(question=question, response=option, user=user)
    response.save()
    try:
        user_score = UserScore.objects.get(user=user, ques_bank=ques_bank)
    except (UserScore.DoesNotExist):
        user_score = UserScore(user=user, ques_bank=ques_bank, score=0)
    if answer.option == option:
        user_score.score = user_score.score + question.score
    user_score.save()
    return dajax.json()