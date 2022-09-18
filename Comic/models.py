from distutils.text_file import TextFile
from pyexpat import model
from telnetlib import STATUS
import this
from tokenize import Special
from typing import overload
from xmlrpc.client import Boolean
from django.db import models
import os
import datetime

from Account.models import Account, Profile
# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=30)
    Special = models.BooleanField(default=False)
    Decreption = models.TextField()

    def __str__(self) -> str:
        return self.Name
class Comic(models.Model):
    STATUS_CHOICES = (
        ("Completed", "Completed"),
        ("Updating", "Updating"),
        ("Draft", "Draft"),
    )
    def update_filename(instance, filename):
        path = "img/banner"
        format = instance.Slug+'.'+ filename.split('.')[-1]
        return os.path.join(path, format)
    Name = models.CharField(max_length=50,default='')
    Author = models.CharField(max_length=40)
    Status = models.CharField(choices=STATUS_CHOICES,default=STATUS_CHOICES[0],max_length=20)
    Views = models.BigIntegerField(default=0)
    Context = models.TextField()
    Slug = models.SlugField()
    Categories = models.ManyToManyField(Category)
    Banner = models.ImageField(upload_to=update_filename, height_field=None, width_field=None, max_length=100,null=True)
    CreatedAt = models.DateTimeField(default=datetime.datetime.now())
    UpdateAt = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self) -> str:
        return self.Name

class Chapter(models.Model):
    def getNumberChapter(self):
        return self.NumberChapter
    def getPreviousChapter(self):
        return str(self.PreviousChapter)
    Comic = models.ForeignKey(Comic,on_delete=models.CASCADE,related_name='chapters')
    NumberChapter = models.FloatField(default=0)
    PreviousChapter = models.OneToOneField("self",on_delete=models.CASCADE,null=True,related_name='chapterprevious')
    NameChapter = models.CharField(max_length=100)
    CreateAt = models.DateTimeField(default=datetime.datetime.now())
    Views = models.BigIntegerField(default=0)
    UpdateAt = models.DateTimeField(default=datetime.datetime.now())
    # def update(self, *args, **kwargs):
    #     # Some Business Logic

    #     # Call super to continue the flow -- from below line we are unable to invoke super
    #     self.Views +=1
    #     super().update(*args, **kwargs) 
    # def get(self, *args, **kwargs):
    #     self.Views+=1
    #     super().update(*args, **kwargs)
    #     super().get(*args, **kwargs)

    def __str__(self) -> str:
        return self.Comic.Name + " "+ str(self.NumberChapter)
class Page(models.Model):
    def update_filename(self,filename):
        path = "img/"+str(self.Chapter.Comic.Slug)+'/'+str(self.Chapter.NumberChapter)
        format = "pages-"+str(self.PageNumber)+'.'+ filename.split('.')[-1]
        return os.path.join(path, format)
    Chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    PageNumber = models.IntegerField(default=0)
    Page = models.ImageField(blank=True,upload_to=update_filename, height_field=None, width_field=None, max_length=100,null=True)
    def __str__(self):
        return self.Chapter.Comic.Name+" "+str(self.Chapter.NumberChapter) +' '+str(self.PageNumber)
    def get(self, *args, **kwargs):
        self.Views+=1
        super().update(*args, **kwargs)
        super().get(*args, **kwargs)

class CommentComic(models.Model):
    Comic = models.ForeignKey(Comic,on_delete=models.CASCADE,related_name='comments')
    Chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE,blank=True,null=True)
    CreateAt = models.DateTimeField(default=datetime.datetime.now())
    Content = models.TextField(blank=False)
    User = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
class RepComment(models.Model):
    Comment = models.ForeignKey(CommentComic,on_delete=models.CASCADE,related_name='replies')
    Content = models.TextField()
    User = models.ForeignKey(Profile,on_delete=models.CASCADE)
    CreateAt = models.DateTimeField(default=datetime.datetime.now())
    