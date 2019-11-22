from django.contrib import admin
from .models import Post ,Comment
# Register your models here.

class PostReg(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','publish',)
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostReg)

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','comment')
admin.site.register(Comment,CommentAdmin)
