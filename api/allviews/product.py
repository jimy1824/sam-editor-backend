from rest_framework import viewsets
from constructor import models
from api.serializers import product_serializer, logo_serializer

from rest_framework.decorators import action
from rest_framework.response import Response


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

    @action(detail=True, methods=['get'], name='product_detail', url_path='product_detail')
    def product_detail(self, request, *args, **kwargs):
        """
        Returns list of courses by country`.
        """
        product_design = self.get_object()
        if product_design.category.key == 'shirt':
            serializer = product_serializer.ProductDetailSerializer(product_design)

            return Response(serializer.data)

        if product_design.category.key == 'vest':
            serializer = product_serializer.VestDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'towel':
            serializer = product_serializer.TowelDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'hat':
            serializer = product_serializer.HatDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'hoodie':
            serializer = product_serializer.HoodieDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'pants':
            serializer = product_serializer.PantDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'tank-top':
            serializer = product_serializer.TankTopDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'coach-jacket':
            serializer = product_serializer.CoachJacDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'bomber-jacket':
            serializer = product_serializer.BomberJacDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'base-ball-shirt':
            serializer = product_serializer.BaseBShirtDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'base-ball-jacket':
            serializer = product_serializer.BaseBJacDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'bag':
            serializer = product_serializer.BagDetailSerializer(product_design)
            return Response(serializer.data)

        if product_design.category.key == 'apron':
            serializer = product_serializer.ApronDetailSerializer(product_design)
            return Response(serializer.data)

        serializer = self.get_serializer(product_design)
        return Response(serializer.data)


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all().order_by('order')
    serializer_classes = {
        'list': product_serializer.CategoryListSerializer,
        'retrieve': product_serializer.CategoryDetailSerializer,
        'category_detail': product_serializer.CategoryDetailSerializer,
    }
    default_serializer_class = product_serializer.CategoryListSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=True, methods=['get'], name='towel', url_path='towel')
    def category_detail(self, request, *args, **kwargs):
        """
        Returns list of courses by country`.
        """
        category_instance = self.get_object()
        serializer = self.get_serializer(category_instance)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='apron', url_path='apron')
    def courses(self, request, *args, **kwargs):
        """

        Returns list of courses by country`.
        """
        category_instance = self.get_object()

        if (category_instance.key == 'apron'):
            qs_apron = models.Apron.objects.all()
            serializer_apron = product_serializer.ApronSerializer(qs_apron, many=True)

        return Response(serializer_apron.data)


class LogoView(viewsets.ModelViewSet):
    queryset = models.DesignImages.objects.all()
    serializer_classes = {
        'list': logo_serializer.LogoSerializer,
    }
    default_serializer_class = logo_serializer.LogoSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
