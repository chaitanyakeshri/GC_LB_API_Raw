from django.shortcuts import get_object_or_404, render 
from .models import Article
from django.http import HttpResponse


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/articles_list.html',{'articles':articles})

'''def article_detail(request,):
    return HttpResponse(slug)
    '''
def article_detail(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    return HttpResponse(article_slug)