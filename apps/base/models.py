from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(
        max_length=400,
        verbose_name='Вопрос'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
      
        
class Answers(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE,
        related_name='answers'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Вариант ответов'
    )
    is_correct = models.BooleanField(
        verbose_name='Правильный ответ',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    
    
class QuizResult(models.Model):
    user_name = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя',
        blank=True, null=True
    )
    total_questions = models.IntegerField(
        verbose_name='Общее количество вопросов'
    )
    correct_answers = models.IntegerField(
        verbose_name='Правильных ответов'
    )
    score = models.IntegerField(
        verbose_name='Баллы'
    )
    completed_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата прохождения'
    )
    
    def __str__(self):
        return f'Результат: {self.correct_answers}/{self.total_questions} баллов'
    
    class Meta:
        verbose_name = 'Результат викторины'
        verbose_name_plural = 'Результаты викторины'