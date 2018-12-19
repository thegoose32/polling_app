from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Aggregate
from django.forms import ModelForm

from .models import Choice, Question, Department
from .forms import NewQuestionForm, DeptForm

#Forms

def newQuestionForm(request):
    if request.method == 'Post':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = NewQuestionForm()
    return render(request, 'polls/newQuestion.html', {'form': form})


def deptForm(request):
    if request.method == 'POST':
        a = Department.get(id=request.GET['id'])
        form = DeptForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:department'))
    else:
        form = DeptForm()
    return render(request, 'polls/newDept.html', {'form': form})

def newAnswerForm(request):
    if request.method == 'POST':
        form = NewAnswerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = NewAnswerForm()
    return render(request, 'polls/newQuestion.html', {'form': form})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]

class DeptView(generic.ListView):
    queryset = Department.objects.order_by('number')
    model = Department
    template_name = 'polls/department.html'
    context_object_name = 'dept_list'

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

#def newQuestionForm(request):
#    return render(request, 'polls/newQuestion.html') 

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

def deleteDept(request, dept_id):
    dept = get_object_or_404(Department, pk=dept_id)
    dept.delete()
    return HttpResponseRedirect(reverse('polls:department'))

def editDept(request, dept_id):
    if request.method == 'POST':
        a = Department.get(id=dept_id)
        form = DeptForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:department'))
    return render(request, 'polls/newDept.html', {'form': form})
