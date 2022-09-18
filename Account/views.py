from email import message
from os import name
from tokenize import Name
from django.shortcuts import render,HttpResponseRedirect,HttpResponsePermanentRedirect,redirect
from django.views import View
from django.views.generic import CreateView
from .forms import *
from .models import Account
from django.contrib import messages
from django.core.cache import cache
from django.urls import reverse
import json
# Create your views here.

class Login(View):
    def get(self,request):
        f = LoginForm()
        context = {
            'form':f
        }
        return render(request, 'Account/login.html',context)

    def post(self,request):
        form = request.POST
        email = form['Email']
        password = form['Password']
        acc = Account.objects.filter(Email=email,Password=password).first()
        if acc :
            request.session['name']=acc.profile.Name
            request.session['id']=acc.id
        else:
            # messages.
            messages.error(self.request,'Tài khoản không tồn tại')
            return HttpResponseRedirect(self.request.path_info)
        return redirect('home')

class Logout(View):
    def get(self,request):
        del request.session['name']
        del request.session['id']
        return redirect('login')

class Register(View):
    def get(self,request):
        if 'id' not in request.session:
            form = UserCreationMultiForm()
            return render(request,'Account/register.html',context={'form':form})
        else:
            return redirect('home')
    def post(self,request):
        form = UserCreationMultiForm(request.POST, request.FILES)
        form.errors.clear()
        if form.is_valid():
            form.save()
            profile = Profile.objects.filter(Account__Email = form['user']['Email'].value()).first()
            request.session['name']=profile.Name
            request.session['id']=profile.id
            return redirect('home')
        return render(request,'Account/register.html',context={'form':form})