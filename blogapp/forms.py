from django import forms
from .models import Comment ,Post
from django.contrib.auth.models import User
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','comment')

class SignupForms(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class Updateuser(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body','status']
class Createform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body','status']
