# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Blogger(models.Model):
    title = models.CharField(max_length=230)
    body = models.TextField()
    dR   = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'dR')
    
admin.site.register(Blogger, BlogPostAdmin)
    
