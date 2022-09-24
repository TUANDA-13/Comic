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
        profile = Profile.objects.filter(Account__Email=email,Account__Password=password).first()
        if profile :
            request.session['name']=profile.Name
            request.session['id']=profile.id
            request.session['avatar']=profile.Avatar.url
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
    
class ProfileView(View):
    def get(self,request):
        id = request.session['id']
        if(id):
            profile = Profile.objects.get(id = id)
            profileForm = ProfileUpdateForm(instance=profile)
            return render(request,'Account/profile.html',context={
                'form':profileForm,
            })
        else:
            return redirect('login')
        
    def post(self,request):
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(pk = request.session['id'])
            profile.Name = form['Name'].value()
            profile.Gender = form['Gender'].value()
            print(form['Avatar'].value())
            if(form['Avatar'].value()!='default.png'):
                profile.Avatar = form['Avatar'].value()
            profile.Phone = form['Phone'].value()
            profile.save()
            return redirect('profile')
        return render(request,'Account/profile.html',context={'form':form})
        
        
def ChangePassword(request):
    pass
        