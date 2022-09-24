from winreg import QueryInfoKey, QueryValue
from Comic.models import Category, Chapter, Comic
from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Count, Sum

from Viewed.models import Viewed
from .models import *
import random
import math
from random import shuffle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils.lib import getCategory, getPaginator

class ComicView(View):
    def get(self, request, id=1):
        categories_col_1,categories_col_2,categories_col_3,categories_col_4 = getCategory()
        comic = Comic.objects.get(pk=id)
        # suggest_comic = Comic.objects.exclude(pk=id)[:4]
        chapters = Chapter.objects.exclude(pk=id).values('Comic').annotate(Views=Sum('Views')).annotate(Chapters=Count('NumberChapter')).values('Comic__Name','Views','Comic__Banner','Chapters','Comic__id','Comic__Slug').order_by('-Comic__UpdateAt')
        suggest_comic = sorted(chapters, key=lambda x: random.random())[:4]
        chapters = Chapter.objects.filter(Comic__id=id)
        categories = comic.Categories.all()
        print(chapters)
        context = {
            'categories_col_1': categories_col_1,
            'categories_col_2': categories_col_2,
            'categories_col_3': categories_col_3,
            'categories_col_4': categories_col_4,
            'comic': comic,
            'chapters': chapters,
            'categories': categories,
            'suggest_comic':suggest_comic,
        }
        return render(request, 'Comic/comic.html', context)
    def post(self, request, id=1):
        if request.method == "POST":
            
            content = request.POST["comment"]
            comment = ComicComment(Comic=Comic.objects.get(pk=id),
                                   Content = content,
                                   User=Profile.objects.get(pk=request.session['id']))
            if((request.POST["type"])=='reply'):
                id_comment = request.POST["id-comment"]
                comment.Reply = ComicComment.objects.get(pk=id_comment)
            # print(comment.Chapter)
            comment.save()
        return redirect(request.path_info)

class CategoryView(View):
    def get(self, request, id=0):
        if id==0:
            chapters = Chapter.objects.values('Comic').annotate(Views=Sum('Views')).annotate(Chapters=Count('NumberChapter')).filter(Comic__Categories__id=id).values(
            'Comic__Name', 'Views', 'Comic__Banner', 'Chapters', 'Comic__id', 'Comic__Slug').order_by('-Comic__UpdateAt')
        else:
            chapters = Chapter.objects.values('Comic').annotate(Views=Sum('Views')).annotate(Chapters=Count('NumberChapter')).values(
            'Comic__Name', 'Views', 'Comic__Banner', 'Chapters', 'Comic__id', 'Comic__Slug').order_by('-Comic__UpdateAt')
        pageNumber = request.GET.get('page')
        categories_col_1,categories_col_2,categories_col_3,categories_col_4 = getCategory()
        chapters = getPaginator(chapters,pageNumber)
        category = Category.objects.get(pk=id)
        context = {
            'categories_col_1': categories_col_1,
            'categories_col_2': categories_col_2,
            'categories_col_3': categories_col_3,
            'categories_col_4': categories_col_4,
            'chapters': chapters,
            'category': category,
        }
        # print(os.path.)
        return render(request, 'Comic/category.html', context)

class ChapterView(View):
    def get(self,request,comic_id=1,chapter_id=1):
        categories_col_1,categories_col_2,categories_col_3,categories_col_4 = getCategory()
        chapter = Chapter.objects.all()[chapter_id-1]
        pages = Page.objects.filter(Chapter__id = chapter_id).order_by('PageNumber')
        chapter.Views += 1
        chapter.save()
        if('id' in request.session):
            user_id = request.session['id']
            viewed  = Viewed.objects.filter(Profile__id = user_id, Chapter__id = chapter_id,Comic__id = comic_id)
            if viewed.count() == 0:
                viewed = Viewed.objects.create(Profile = Profile.objects.get(pk = user_id),
                                               Chapter = Chapter.objects.get(pk = chapter_id),
                                               Comic = Comic.objects.get(pk = comic_id))
                viewed.save()
        context = {
            'categories_col_1': categories_col_1,
            'categories_col_2': categories_col_2,
            'categories_col_3': categories_col_3,
            'categories_col_4': categories_col_4,
            'pages':pages,
            'chapter':chapter,
        }
        return render(request,'Comic/chapter.html',context)
    def post(self,request,comic_id=1,chapter_id=1):
        if request.method == "POST":
            content = request.POST["comment"]
            comment = ComicComment(Comic=Comic.objects.get(pk=comic_id),
                                   Chapter=Chapter.objects.get(pk=chapter_id),
                                   Content = content,
                                   User=Profile.objects.get(pk=request.session['id']))
            if((request.POST["type"])=='reply'):
                id_comment = request.POST["id-comment"]
                comment.Reply = ComicComment.objects.get(pk=id_comment)
            comment.save()
        return redirect(request.path_info)

def Test(request):
    chapter = Chapter.objects.prefetch_related('chapterprevious')
    chapter = Chapter.objects.all()[5].chapterprevious.id
    print(chapter)
    return render(request,'Comic/test.html',context = {'chapter':chapter})


