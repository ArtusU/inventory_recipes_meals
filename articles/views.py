from operator import contains
from re import A
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ArticleForm
from .models import Article


def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.all()
    if query is not None:
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        qs = Article.objects.filter(lookups)
        # qs = Article.objects.search(query)
    context = {
        "object_list": qs
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
        return redirect(article_object.get_absolute_url())
    return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
