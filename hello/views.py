from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from hello.models import TOdoItem
import datetime

# Create your views here.


def todoView(request):
    all_todo_item = TOdoItem.objects.all()
    dic = {'all_item':all_todo_item }
    return render(request, 'todo.html', dic)

def add_todo(request):
    new_item = TOdoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delete_todo(request, todo_id):
    item_to_delete = TOdoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')





