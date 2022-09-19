from django.views import View
from django.db.models import Sum,Count
# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from Viewed.models import *
from utils.lib import getPaginator, getCategory
class ViewedComic(View):
    def get(self,request):
        chapters = ''
        if('id' in request.session):
            user_id = request.session['id']
        # chapters = Viewed.objects.filter(Profile = Profile.objects.get(pk=1)).values_list('Comic','Comic__id','Comic__Name','Comic__Banner','Comic__CreatedAt','Comic__Views','Comic__Status','Comic__Author').distinct('id')
            comics = Viewed.objects.filter(Profile = Profile.objects.get(pk=user_id)).values('Comic').distinct()
            comic_ids = []
            for i in comics:
                comic_ids.append(int(i["Comic"]))
            chapters = Chapter.objects.values('Comic').annotate(Views=Sum('Views')).annotate(Chapters=Count('NumberChapter')).filter(Comic__id__in=comic_ids).values(
                'Comic__Name', 'Views', 'Comic__Banner', 'Chapters', 'Comic__id', 'Comic__Slug').order_by('-Comic__UpdateAt')
        chapters = getPaginator(chapters,request.GET.get('page'))
        categories_col_1,categories_col_2,categories_col_3,categories_col_4 = getCategory()
        return render(request, 'Viewed/history.html',context = {
            'chapters':chapters,
            'categories_col_1': categories_col_1,
            'categories_col_2': categories_col_2,
            'categories_col_3': categories_col_3,
            'categories_col_4': categories_col_4,
        })