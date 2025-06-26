from django.contrib import admin

from apps.base.models import Question, Answers
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    