from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.models import task
from todoapp.forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 't'

class taskdetail(DetailView):
    model=task
    template_name = 'detail.html'
    context_object_name = 'Task'

class taskupdateview(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:detailview',kwargs={'pk':self.object.id})


class taskdeleteview(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:home')



def home(request):
    t1 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date =request.POST.get('date','')
        Task = task(name=name,priority=priority,date=date)
        Task.save()
    return render(request,"home.html",{'t':t1})

#
# def details(request):

#      return render(request,'detail.html',{'t':t1})


def delete(request,taskid):
    if request.method == 'POST':
        t2 = task.objects.get(id=taskid)
        t2.delete()
        return redirect("/")


    return render(request,"delete.html")

def update(request,id):
    t3=task.objects.get(id=id)
    fm=todoform(request.POST or None,instance=t3)
    if fm.is_valid():
        fm.save()
        return redirect("/")
    return render(request,"edit.html",{'form':fm,'task':t3})

#
#
