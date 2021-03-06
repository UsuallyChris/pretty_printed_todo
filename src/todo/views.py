from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
  todo_list = Todo.objects.order_by('id')
  context = {'todo_list' : todo_list}
  return render(request, 'todo/index.html', context)