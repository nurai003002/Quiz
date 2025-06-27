from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.base.models import Question, Answers, QuizResult
import json

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

@csrf_exempt
def check_answer(request):
    """AJAX вьюха для проверки отдельного ответа"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question_id = data.get('question_id')
            selected_answer = data.get('selected_answer')
            
            # Находим правильный ответ для данного вопроса
            correct_answer = Answers.objects.filter(
                question_id=question_id, 
                is_correct=True
            ).first()
            
            if correct_answer and correct_answer.title == selected_answer:
                return JsonResponse({
                    'is_correct': True,
                    'message': 'Правильно! +1 балл',
                    'correct_answer': correct_answer.title
                })
            else:
                return JsonResponse({
                    'is_correct': False,
                    'message': 'Неправильно! Правильный ответ: ' + (correct_answer.title if correct_answer else 'Не найден'),
                    'correct_answer': correct_answer.title if correct_answer else None
                })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Метод не разрешен'}, status=405)

@csrf_exempt
def submit_quiz(request):
    """Обработка финального результата викторины"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            answers = data.get('answers', {})
            
            total_questions = Question.objects.count()
            correct_count = 0
            
            # Проверяем все ответы
            for question_id, selected_answer in answers.items():
                correct_answer = Answers.objects.filter(
                    question_id=question_id,
                    is_correct=True
                ).first()
                
                if correct_answer and correct_answer.title == selected_answer:
                    correct_count += 1
            
            # Сохраняем результат
            quiz_result = QuizResult.objects.create(
                total_questions=total_questions,
                correct_answers=correct_count,
                score=correct_count
            )
            
            return JsonResponse({
                'total_questions': total_questions,
                'correct_answers': correct_count,
                'score': correct_count,
                'percentage': round((correct_count / total_questions) * 100, 2) if total_questions > 0 else 0,
                'result_id': quiz_result.id
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Метод не разрешен'}, status=405)

def quiz_result(request, result_id):
    """Страница с результатами викторины"""
    try:
        result = QuizResult.objects.get(id=result_id)
        # Выводим результат в терминал
        print("="*50)
        print("РЕЗУЛЬТАТЫ ВИКТОРИНЫ")
        print("="*50)
        print(f"Правильных ответов: {result.correct_answers}")
        print(f"Всего вопросов: {result.total_questions}")
        print(f"Баллы: {result.score}")
        print(f"Процент: {round((result.correct_answers / result.total_questions) * 100, 2)}%")
        print(f"Дата прохождения: {result.completed_at}")
        print("="*50)
        
        return JsonResponse({
            'message': 'Результаты выведены в терминал',
            'result': {
                'correct_answers': result.correct_answers,
                'total_questions': result.total_questions,
                'score': result.score,
                'percentage': round((result.correct_answers / result.total_questions) * 100, 2)
            }
        })
    except QuizResult.DoesNotExist:
        return JsonResponse({'error': 'Результат не найден'}, status=404)