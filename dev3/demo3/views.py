from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404

from .models import Problem,Option

# Create your views here.


def index(request):
    listp= Problem.objects.all()
    return render(request,'demo3/index.html',{'listp':listp})


def detail(request,id):
    wt=Problem.objects.get(pk=id)
    return render(request,'demo3/detail.html',{'wt':wt})


def poll(request,id):
    try:
        oid=request.POST['wname']
        wt = Problem.objects.get(pk=id)
        xuan=Option.objects.get(pk=oid)
        xuan.oshu+=1
        xuan.save()
        return render(request,'demo3/poll.html',{'wt':wt,'pshu':oid})
    except:

        return HttpResponse('你都没选，还想跑！！！')

