from django import forms
from django.forms import fields, widgets

from .models import question
from .models import game
from .models import mark

class GameForm(forms.ModelForm):
    class Meta:
        model = game
        fields=['game_name','game_desc','game_img']

class MarksForm(forms.ModelForm):
    class Meta:
        Model = mark
        fields=['user_id','game_id','mark']


class QuestionForm(forms.ModelForm):
    class Meta:
        model =question
        fields=['question','option1','option2','option3','option4']
        widgets={
            'option1':forms.CheckboxInput(),
            'option2':forms.CheckboxInput(),
            'option3':forms.CheckboxInput(),
            'option4':forms.CheckboxInput(),


        }
        labels ={

            'option1':'1',
        }