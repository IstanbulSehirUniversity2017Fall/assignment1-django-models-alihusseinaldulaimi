# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
from models import Article, Tags

admin.site.register(Article)
admin.site.register(Tags)
