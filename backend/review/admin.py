from django.contrib import admin
from .models import Comment, Rating

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['review_text', 'product', 'user', 'updated_at']
    list_filter = ['product', 'user']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'score']
    list_filter = ['product', 'user']

