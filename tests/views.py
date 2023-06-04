from django.shortcuts import render, get_object_or_404, redirect
from tests.models import Test, Question, Answer, UserAnswer
from django.http import HttpResponseBadRequest
                        

def test_list(request):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'tests/test_list.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Test, Question, UserAnswer

@login_required
def submit_answers(request, test_id):
    if request.method == 'POST':
        test = Test.objects.get(pk=test_id)
        questions = Question.objects.filter(test=test)
        user = request.user

        for question in questions:
            answer_key = f'answers_{question.id}'
            custom_answer_key = f'answer_{question.id}'

            if answer_key in request.POST:
                chosen_answers = request.POST.getlist(answer_key)
                for chosen_answer in chosen_answers:
                    is_correct = chosen_answer == question.correct_answer
                    UserAnswer.objects.create(
                        user=user,
                        question=question,
                        chosen_answer=chosen_answer,
                        is_correct=is_correct
                    )

            elif custom_answer_key in request.POST:
                chosen_answer = request.POST[custom_answer_key]
                is_correct = chosen_answer == question.correct_answer
                UserAnswer.objects.create(
                    user=user,
                    question=question,
                    chosen_answer=chosen_answer,
                    is_correct=is_correct
                )

        return redirect('test_detail', test_id=test_id)

    else:
        return redirect('test_detail', test_id=test_id)



def test_detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test_id).prefetch_related('answers')
    context = {'test': test,
               'questions': questions
               }
    return render(request, 'tests/test_detail.html', context)


#prefetch_related('answers') для предварительной загрузки связанных объектов Answer для каждого вопроса. 
#Это помогает избежать дополнительных запросов к базе данных при доступе к связанным объектам внутри цикла.