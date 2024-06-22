from .models import Todo
from django import forms


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = '__all__'
		widgets = {
			'task': forms.Textarea(attrs={'class': 'form-control'}),
		}