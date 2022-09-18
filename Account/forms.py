from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django.forms import ModelForm,Textarea,PasswordInput,EmailField,TextInput,ImageField,ChoiceField,CharField,ValidationError
from django.core.exceptions import ObjectDoesNotExist
from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User
import re
from .models import *
class LoginForm(ModelForm):
    class Meta:
        model = Account
        fields = ['Email','Password']
        widgets = {
            'Email' : TextInput(attrs={'title' :'Email','class':'email__input','placeholder':'Email'}),
            'Password' : PasswordInput(attrs={'title' :'Password','class':'password__input','placeholder':'Password'}),        
        }
class AccountRegisterForm(ModelForm):
    ConfirmPassword = CharField(widget=PasswordInput(render_value = True,attrs={'title' :'Password','class':'password__input','placeholder':'Confirm password'}))
    class Meta:
        model = Account
        fields = ['Email','Password']
        widgets = {
            'Email' : TextInput(attrs={'title' :'Email','class':'email__input','placeholder':'Email'}),
            'Password' : PasswordInput(attrs={'title' :'Password','class':'password__input','placeholder':'Password'}),        
        }
    def save(self, commit=True):
    # do something with self.cleaned_data['temp_id']
        return super(AccountRegisterForm, self).save(commit=commit)
    def clean_ConfirmPassword(self):
        if 'Password' in self.cleaned_data:
            password = self.cleaned_data['Password']
            confirmPassword = self.cleaned_data['ConfirmPassword']
            if password == confirmPassword:
                return password
        raise ValidationError("Mật khẩu không hợp lệ")
    def clean_Email(self):
        email = self.cleaned_data['Email']
        try:
            acc = Account.objects.filter(Email=email).count()
            if acc > 0:
                raise ValidationError("Tài khoản đã tồn tại")
        except ObjectDoesNotExist:
            return email
        return email
        

class ProfileRegisterForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['Name','Phone','Gender','Avatar']
        widgets = {
            'Name': TextInput(attrs={'class':'Name__input','placeholder':'Full name'}),
            'Phone':TextInput(attrs={'class':'Phone__input','placeholder':'Phone'}),
            # 'Avatar':ImageField(),
        }
class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': AccountRegisterForm,
        'profile': ProfileRegisterForm,
    }
    def save(self, commit=True):
        objects = super(UserCreationMultiForm, self).save(commit=False)

        if commit:
            user = objects['user']
            user.save()
            profile = objects['profile']
            profile.Account = user
            profile.save()
        return objects