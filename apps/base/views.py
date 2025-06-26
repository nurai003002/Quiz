from django.shortcuts import render

from apps.base.models import Question, Answers
# Create your views here.
def index(request):
    questions = Question.objects.all()
    answers = Answers.objects.all()
    return render(request, 'index.html', locals())