import math
from pydoc_data.topics import topics
from django.shortcuts import redirect, render 
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import math
from django.db.models import Avg, Max, Min,Count,Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Comic.models import Category, Chapter
def Base(request):
    return render(request,'base.html')


class Home(View):
    def get(self,request):
        categories = Category.objects.all()
        categories_per_col = math.ceil(len(categories)/4)
        categories_col_1 = categories[:categories_per_col]
        categories_col_2 = categories[categories_per_col:2*categories_per_col]
        categories_col_3 = categories[categories_per_col*2:3*categories_per_col]
        categories_col_4 = categories[categories_per_col*3:]
        chapters = Chapter.objects.values('Comic').annotate(Views=Sum('Views')).annotate(Chapters=Count('NumberChapter')).values('Comic__Name','Views','Comic__Banner','Chapters','Comic__id','Comic__Slug').order_by('-Comic__UpdateAt')
        paginator = Paginator(chapters, 8)  
        page_number = request.GET.get('page')
        suggest_chapter = chapters.order_by('Views')[1:7]
        hot_chapter = chapters.order_by('Views')[0]
        try:
            chapters = paginator.page(page_number)
        except PageNotAnInteger:
            chapters = paginator.page(1)
        except EmptyPage:
            chapters = paginator.page(paginator.num_pages)
        context = {
            'categories_col_1':categories_col_1,
            'categories_col_2':categories_col_2,
            'categories_col_3':categories_col_3,
            'categories_col_4':categories_col_4,
            'chapters':chapters,
            'suggest_chapter':suggest_chapter,
            'hot_chapter':hot_chapter,  
        }
        return render(request,'home.html',context)

