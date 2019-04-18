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
    oid=request.POST['xx']
    Option.objects.get(pk=oid).oshu
