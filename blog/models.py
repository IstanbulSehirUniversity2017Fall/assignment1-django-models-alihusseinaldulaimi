# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    author = models.CharField(max_length=20)
    text = models.TextField()
    article_image = models.CharField(max_length=10000)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
