#from typing_extensions import Required
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.forms import Form
from .models import Project_comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Project_comment
        fields = ['name', 'body']
        widgets = {}   

    name = forms.CharField (
        max_length = 40,
        label='',
        widget=forms.TextInput(
            attrs={
                'style':'background: #d8d8d885; border: solid 0.01rem #b5b2b285; color: black;',
                'placeholder': 'User Name'
            }
        )        
    ) 

    body = forms.CharField(
        label='',  

        widget=forms.Textarea(               
            attrs={
                'style':'background: #d8d8d885; border: solid 0.01rem #b5b2b285; color: black;',                
                'rows': '3',
                'placeholder': 'Write a comment ...'
            }
        )
    )
    