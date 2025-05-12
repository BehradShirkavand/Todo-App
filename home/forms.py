from django import forms
from .models import Todo


# simple form
class TodoCreateForm(forms.Form):
    title = forms.CharField(help_text="gkf")
    body = forms.CharField()
    created_at = forms.DateTimeField(initial='2020-12-30 00:00:00')

# model form
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'