from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from member.models import Person

def home(request):
    return HttpResponse("Hello Preeti, startPage")

# Create your views here.
# def welcome(request):
#     return render(request,'start.html',{'name':'Preeti'})
    

def welcome(request):
    template=loader.get_template('start.html')
    return render(request, 'start.html',{'name' : 'Preeti'})


def add(request):
    val1 = int(request.GET.get('num1'))
    val2 = int(request.GET.get('num2'))
    res = val1 + val2
    return render(request, "result.html", {'result' : res})

def displayDetails(request):
    p = Person.objects.all().values()
    context = {'persondata': p }
    return render(request,'Person.html', context)