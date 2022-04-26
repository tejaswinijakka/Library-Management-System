from django import forms
from django.contrib.auth.models import User
from . import models

class IssueBookForm(forms.Form):
    book_id2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Book Name [book_id]", to_field_name="book_id", label="Book (Name and book_id)")
    name2 = forms.ModelChoiceField(queryset=models.Student.objects.all(), empty_label="Name [Branch] [Roll No]", to_field_name="user", label="Student Details")
    
    book_id2.widget.attrs.update({'class': 'form-control'})
    name2.widget.attrs.update({'class':'form-control'})
