from Comic.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
def getCategory():
    categories = Category.objects.all()
    categories_per_col = math.ceil(len(categories)/4)
    categories_col_1 = categories[:categories_per_col]
    categories_col_2 = categories[categories_per_col:2*categories_per_col]
    categories_col_3 = categories[categories_per_col *
                                    2:3*categories_per_col]
    categories_col_4 = categories[categories_per_col*3:]
    return categories_col_1,categories_col_2,categories_col_3,categories_col_4

def getPaginator(listObject,pageNumber):
    paginator = Paginator(listObject, 4)
    try:
        return paginator.page(pageNumber)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)