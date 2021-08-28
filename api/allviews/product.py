from rest_framework import viewsets
from constructor import models
from api.serializers import product_serializer, logo_serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
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

    @action(detail=True, methods=['get'], name='fabrics', url_path='fabrics')
    def product_fabrics(self, request, *args, **kwargs):
        product_design = self.get_object()
        serializer = self.get_serializer(product_design.fabrics)
        return Response(serializer.data)


class CategoryView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Category.objects.all().order_by('order')
    serializer_classes = {
        'list': product_serializer.CategoryListSerializer,
        'retrieve': product_serializer.CategoryDetailSerializer,
        'category_products': product_serializer.ProductDesignWithCategorySerializers,
    }
    default_serializer_class = product_serializer.CategoryListSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=True, methods=['get'], name='towel', url_path='products')
    def category_products(self, request, *args, **kwargs):
        """
        Returns list of courses by country`.
        """
        category_instance = self.get_object()
        qs = models.ProductDesign.objects.filter(category=category_instance).order_by('name')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class LogoView(viewsets.ModelViewSet):
    queryset = models.DesignImages.objects.all()
    serializer_classes = {
        'list': logo_serializer.LogoSerializer,
    }
    default_serializer_class = logo_serializer.LogoSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=['post'], name='upload_logo', url_path='upload_logo')
    def upload_logo(self, request, *args, **kwargs):
        """
        Returns list of courses by country`.
        """

        try:
            file = request.data['file']
            obj = models.DesignImages(image=file, name=file.name)
            obj.save()
            serializer = self.get_serializer(models.DesignImages.objects.all(), many=True)
        except KeyError:
            raise ParseError("File is not Attached")

        return Response(serializer.data)
