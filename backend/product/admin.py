from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity', 'description', 'category', 'created_at', 'updated_at']
    list_select_related = ('category', )
    search_fields = ('name', )  # Qidiruv maydonlari
    list_filter = ('category',)  # Filtrlash
    ordering = ('-created_at',)
    list_editable = ['price', 'quantity']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


