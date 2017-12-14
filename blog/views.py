# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count
from django.shortcuts import render, HttpResponse, redirect
from models import Article, Tags
from django.http import Http404
# Create your views here.

def index(request):
    try:
        articles = Article.objects.all()
        tags = Tags.objects.all()
        return render(request, "index.html" ,{'articles':articles[::-1],'tags':tags})
    except:
        return HttpResponse("sdfsf")


def blog(request, tag):
    articles_by_tag = Article.objects.all().filter(tag__title=tag)
    tags = Tags.objects.all()
    return render(request, "index.html", {'articles': articles_by_tag[::-1],'tags': tags})


def article(request, id):
    article_by_id = Article.objects.filter(id=id)
    tags = Tags.objects.all()
    context = {'articles': article_by_id,
               'tags': tags}
    return render(request, "index.html", context=context)
