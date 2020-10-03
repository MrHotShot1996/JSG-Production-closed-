from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
# Create your views here.

def home(request):
    return render(request, 'regs/home.html')

def join(request):
    if request.method == 'POST':

        first_name = request.POST.get("Fname")
        last_name = request.POST.get("Lname")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        s = Users(first_name=first_name, last_name=last_name,\
            phone=phone,email=email)
        s.save()
        print(f'{first_name} has signed up')
        context = {
        'first_name':first_name
        }
        return render(request,'regs/success.html',context)
    
    return render(request,'regs/join.html')

def about(request):
    return render(request, 'regs/about.html')