from django.urls import path
from .views import ProductListView, ProductCategoryListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('category/<int:category_id>/', ProductCategoryListView.as_view(), name='product-category-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]