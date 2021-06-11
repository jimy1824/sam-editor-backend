from rest_framework import viewsets
from constructor import models
from api.serializers import product_serializer



# from api.utils.paginator import ResultsSetPagination


class ProductView(viewsets.ModelViewSet):
    queryset = models.ProductDesign.objects.all()
    serializer_classes = {
        'list': product_serializer.ProductDetailSerializer,
        'retrieve': product_serializer.ProductDetailSerializer,
    }
    default_serializer_class = product_serializer.ProductDetailSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_classes = {
        'list': product_serializer.CategoryListSerializer,
    }
    default_serializer_class = product_serializer.CategoryListSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
