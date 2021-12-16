# Create your views here.
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views import generic

class RegistrationView(generic.View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})
    
    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,
            'congratulstions!!! Registered Successfully')
            return redirect('/register',{'form':form})
        return render(request,'register.html',{'form':form})
