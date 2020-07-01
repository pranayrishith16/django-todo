from django.forms import ModelForm, TextInput
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {'text': TextInput(attrs={'class': 'input'})}
