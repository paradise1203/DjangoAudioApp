from django.contrib import admin

from dvach.models import Post
from dvach.models import Comment

admin.site.register(Post)
admin.site.register(Comment)
