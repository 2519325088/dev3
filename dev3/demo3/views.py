from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import Problem,Option

# Create your views here.


def index(request):
    listp= Problem.objects.all()
    return render(request,'demo3/index.html',{'listp':listp})


def detail(request,id):
    wt=Problem.objects.get(pk=id)
    return render(request,'demo3/detail.html',{'wt':wt})


def poll(request,id):
    wt = Problem.objects.get(pk=id)
    oid=request.POST['wname']
    xuan=Option.objects.get(pk=oid)
    xuan.oshu+=1
    xuan.save()
    return render(request,'demo3/poll.html',{'wt':wt,'pshu':oid})

