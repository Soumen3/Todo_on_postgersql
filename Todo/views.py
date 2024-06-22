from django.shortcuts import render, redirect
from .form import TodoForm
from .models import Todo
from django.contrib import messages

# Create your views here.
def home(request):
	context = {}

	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Task added successfully')
			return redirect('home')
		else:
			messages.error(request, 'Form is invalid')
	form = TodoForm()
	context['form'] = form
	Todos = Todo.objects.all().order_by('-created')
	context['Todos'] = Todos
	return render(request, 'todo/home.html', context)


def delete(request, id):
	Todo.objects.filter(id=id).delete()
	messages.success(request, 'Task deleted successfully')
	return redirect('home')

def edit_task(request, id):
	context = {}
	task = Todo.objects.get(id=id)
	if request.method == 'POST':
		form = TodoForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			messages.success(request, 'Task updated successfully')
			return redirect('home')
		else:
			messages.error(request, 'Form is invalid')

	form = TodoForm(instance=task)
	context['form'] = form
	Todos = Todo.objects.all().order_by('-created')
	context['Todos'] = Todos
	return render(request, 'todo/home.html', context)