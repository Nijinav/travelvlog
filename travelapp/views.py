from django.shortcuts import render
from django.http import HttpResponse
from.models import place
# Create your views here.
def fun(request):
    obj=place.objects.all()
    return render(request,"index.html",{'results':obj})
def addition(request):
    number1=int(request.POST["num1"])
    number2=int(request.POST["num2"])
    number3=number1+number2
    return render(request,"result.html",{"addition":number3})
