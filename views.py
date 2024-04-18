from django.shortcuts import render,redirect
from django.http import HttpResponse
from .import models
 

# Create your views here.

def todo(request):

    return render(request,'index.html')



def FormHandle(request):
    data = dict(request.GET)

    T_id = int(data['T_id'][0])
    T_name = data['T_name'][0]
    T_description = data['T_description'][0]

    data = models.Todo(T_id,T_name,T_description)
    data.save()

    return HttpResponse("<h1> ADD TASK SUCCESSFULLY </h1>")


def updatetask(request):
    data = dict(request.GET)
    
    uT_id = int(data['uT_id'][0])
    uT_name = data['uT_name'][0]
    uT_description = data['uT_description'][0]

    data = models.Todo.objects.filter(T_id=uT_id).update(T_id=uT_id,T_name=uT_name,T_description=uT_description,)

    return redirect('/seealltask',{'update':data})


 
def deletetask(request):
    data = dict(request.GET)
    uT_id = int(data['uT_id'][0])

    models.Todo.objects.filter(T_id = uT_id).delete()

    return redirect('/seealltask')


def seealltask(request):
    data = list(models.Todo.objects.all().values())

    return render(request,'seealltask.html',{'task':data})