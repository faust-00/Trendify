from django.contrib import admin
from .models import Order, OrderItem, Card, CardItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'created_at']
    list_select_related = ('user', )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'created_at']
    list_select_related = ('order', )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    list_select_related = ('user', )


@admin.register(CardItem)
class CardItemAdmin(admin.ModelAdmin):
    list_display = ['card', 'product', 'created_at']
    list_select_related = ('card', )