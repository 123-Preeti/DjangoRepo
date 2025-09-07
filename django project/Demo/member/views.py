from django.shortcuts import render
from django.http import HttpResponse
from member.models import Person

def home(request):
    return HttpResponse("Hello Preeti, this is very first Django app!")

# Create your views here.
def displayDetails(request):
    p=Person.objects.all().values()
    context={
        'persondata':p
    }
    return render(request,'Person.html',context)