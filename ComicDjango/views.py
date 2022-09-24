from pydoc_data.topics import topics
from django.shortcuts import redirect, render 
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min,Count,Sum
from Comic.models import Category, Chapter
from Comic.models import Comic
from utils.lib import getCategory, getPaginator
def Base(request):
    return render(request,'base.html')


class Home(View):
    def get(self,request):
        categories_col_1,categories_col_2,categories_col_3,categories_col_4 = getCategory()
        chapters = Chapter.objects.values('Comic').annotate(Views=Sum('Views')).annotate(Chapters=Count('NumberChapter')).values('Comic__Name','Views','Comic__Banner','Chapters','Comic__id','Comic__Slug').order_by('-Comic__UpdateAt')
        comics = Comic.objects.prefetch_related('chapters').annotate(view=Sum('Views'))
        for i in comics:
            print(i)
        print(comics)
        pageNumber = request.GET.get('page')
        suggest_chapter = chapters.order_by('Views')[1:7]
        hot_chapter = chapters.order_by('Views')[0]
        chapters = getPaginator(chapters,pageNumber)
        context = {
            'categories_col_1':categories_col_1,
            'categories_col_2':categories_col_2,
            'categories_col_3':categories_col_3,
            'categories_col_4':categories_col_4,
            'chapters':chapters,
            'suggest_chapter':suggest_chapter,
            'hot_chapter':hot_chapter,  
            'comics':comics,
        }
        return render(request,'home.html',context)

