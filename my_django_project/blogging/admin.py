from django.contrib import admin
from .models import Post,blog_comment

admin.site.register((Post,blog_comment))

