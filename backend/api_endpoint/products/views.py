from product.models import Product
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer


class ProductCategoryListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category__id=category_id)


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

