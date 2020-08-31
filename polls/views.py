from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, UserAnswer
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    questions = Questions.objects.all()
    score = 0
    if request.method == 'POST':
        for question in questions:
            fields = request.POST[str(question.id)]
            if fields == question.answer:
                score += 5
            # for answer in user_answers:
            #     if answer.answer == question.answer:
            #         print('You got it')
        return HttpResponse(f'The score is {score}')
    else:
        context = {'questions': questions}
        return render(request, 'polls/index.html', context)


def result(request):
    pass
    # questions = Question.objects.all()
    # answer = Answer.objects.all()
    # correct_answers = answer.filter(is_correct=True)
    # user_answer = UserAnswer.objects.all()
    # total = 0
    # for correct_answer in correct_answers:
    #     pass
    # for answer in user_answer:
    #     if answer.answer == 'Abuja' and answer.answer == 'Washington':
    #         total += 10
    #     elif answer.answer == 'Abuja' or answer.answer == 'Washington':
    #         total += 5
    # print(total)
    #  #
    # # for answer in user_answer:
    # #     print(answer)
    # context = {'user_answer': user_answer}
    # return render(request, 'polls/results.html', context)


