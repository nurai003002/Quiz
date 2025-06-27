from django.urls import path
from apps.base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check-answer/', views.check_answer, name='check_answer'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
    path('quiz-result/<int:result_id>/', views.quiz_result, name='quiz_result'),
]