from django_quill.forms import QuillFormField
from django import forms

class ProjectForm(forms.Form):
    content = QuillFormField()