from django.shortcuts import render

from apps.base.models import Question
# Create your views here.
def index(request):
    question = Question.objects.latest('id')
    return render(request, 'index.html', locals())