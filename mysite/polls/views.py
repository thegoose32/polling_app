from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def newQuestionForm(request):
    return render(request, 'polls/newQuestion.html') 

def newQuestion(request):
    #Create instance of Question class
    new_question = Question()
    new_question.question_text = request.POST.get('question_text')
    new_question.pub_date = timezone.now()
    new_question.save()
    return HttpResponseRedirect(reverse('polls:index'))

def deleteQuestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return HttpResponseRedirect(reverse('polls:index'))

class newAnswerFormView(generic.DetailView):
    model = Question
    template_name = 'polls/newAnswer.html'

def newAnswerSubmit(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    new_answer = Choice()
    new_answer.choice_text = request.POST.get('choice_text')
    new_answer.question = question
    new_answer.save()
    return HttpResponseRedirect(reverse('polls:index'))

def deleteAnswer(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    question = get_object_or_404(Question, pk=choice.question.id)
    choice.delete()
    return HttpResponseRedirect(reverse('polls:newAnswerForm', args=(question.id,)))
