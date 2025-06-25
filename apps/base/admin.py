from django.contrib import admin

from apps.base.models import Question, Answers
# Register your models here.
class AnswerTabularInline(admin.TabularInline):
    model = Answers
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    inlines = (AnswerTabularInline, )
    