from django import forms
from .models import Planet, Candidate, Test


class CandidateForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    homeplanet = forms.ModelChoiceField(queryset=Planet.objects.all())
    age = forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = Candidate
        fields = ['name', 'homeplanet', 'age', 'email']


class TestForm(forms.ModelForm):
    order_code = forms.CharField(max_length=30)
    question1 = forms.CharField(max_length=50)
    answer1 = forms.ChoiceField(choices=((1, "Yes"), (2, "Nope")))
    question2 = forms.CharField(max_length=50)
    answer2 = forms.ChoiceField(choices=((1, "Yes"), (2, "Nope")))
    question3 = forms.CharField(max_length=50)
    answer3 = forms.ChoiceField(choices=((1, "Yes"), (2, "Nope")))

    class Meta:
        model = Test
        fields = ['order_code', 'question1', 'answer1',
                  'question2', 'answer2', 'question3', 'answer1'
                  ]
