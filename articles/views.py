from operator import contains
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article
# Create your views here.

def article_search_view(request):
    try:
        query = request.get("q")
    except:
        query = None
        
    article_obj = None
    if query is not None:
        article_obj = Article.objects.filter(Q(title__contains=query))
        print(article_obj)
    context = {
        "object": article_obj,
        "query": query,
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # context['object'] = article_object
        # context['created'] = True
        return render(request, "articles/create.html", context=context)
    return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
