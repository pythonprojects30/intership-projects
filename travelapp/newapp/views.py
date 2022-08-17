from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import person

# Create your views here.
def tb(request):
    obj = place.objects.all()
    return render(request,"index.html",{'display':obj})

def face(request):
    obj1 = person.objects.all()
    return render(request,"index.html",{'display1':obj1})