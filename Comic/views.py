from winreg import QueryInfoKey, QueryValue
from Comic.models import Category, Chapter, Comic
from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Avg, Max, Min, Count, Sum
from .models import *
import random
import math
from random import shuffle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class ComicInfo(View):
    def get(self, request, id=1):
        categories = Category.objects.all()
        categories_per_col = math.ceil(len(categories)/4)
        categories_col_1 = categories[:categories_per_col]
        categories_col_2 = categories[categories_per_col:2*categories_per_col]
        categories_col_3 = categories[categories_per_col *
                                      2:3*categories_per_col]
        categories_col_4 = categories[categories_per_col*3:]
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
        paginator = Paginator(chapters, 4)
        page_number = request.GET.get('page')
        categories = Category.objects.all()
        categories_per_col = math.ceil(len(categories)/4)
        categories_col_1 = categories[:categories_per_col]
        categories_col_2 = categories[categories_per_col:2*categories_per_col]
        categories_col_3 = categories[categories_per_col *
                                      2:3*categories_per_col]
        categories_col_4 = categories[categories_per_col*3:]
        try:
            chapters = paginator.page(page_number)
        except PageNotAnInteger:
            chapters = paginator.page(1)
        except EmptyPage:
            chapters = paginator.page(paginator.num_pages)
        category = Category.objects.get(pk=id)

        context = {
            'categories_col_1': categories_col_1,
            'categories_col_2': categories_col_2,
            'categories_col_3': categories_col_3,
            'categories_col_4': categories_col_4,
            'chapters': chapters,
            'category': category,
        }
        return render(request, 'Comic/category.html', context)

class ChapterView(View):
    def get(self,request,id=1,id_chap=1):
        categories = Category.objects.all()
        categories_per_col = math.ceil(len(categories)/4)
        categories_col_1 = categories[:categories_per_col]
        categories_col_2 = categories[categories_per_col:2*categories_per_col]
        categories_col_3 = categories[categories_per_col *
                                      2:3*categories_per_col]
        categories_col_4 = categories[categories_per_col*3:]
        chapter = Chapter.objects.all()[id_chap-1]
        pages = Page.objects.filter(Chapter__id = id_chap).order_by('PageNumber')
        chapter.Views += 1
        chapter.save()
        context = {
            'categories_col_1': categories_col_1,
            'categories_col_2': categories_col_2,
            'categories_col_3': categories_col_3,
            'categories_col_4': categories_col_4,
            'pages':pages,
            'chapter':chapter,
        }
        return render(request,'Comic/chapter.html',context)
    def post(self,request,id=1,id_chap=1):
        if request.method == "POST":
            content = request.POST["comment"]
            comment = ComicComment(Comic=Comic.objects.get(pk=id),
                                   Chapter=Chapter.objects.get(pk=id_chap),
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


