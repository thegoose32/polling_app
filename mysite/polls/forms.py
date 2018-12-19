from django import forms
from .models import Department

class NewQuestionForm(forms.Form):
    question_text = forms.CharField(label = "Question", max_length=100)

class NewAnswerForm(forms.Form):
    choice_text = forms.CharField(label = "Answer", max_length=100)

class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'number', 'head']
