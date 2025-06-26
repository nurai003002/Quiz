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