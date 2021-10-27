from rest_framework import viewsets
from constructor import models
from api.serializers import product_serializer, logo_serializer, sublimation_serializer, component_serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from django.http import HttpResponse
from rest_framework.response import Response

from constructor.models import ProductDesign, ComponentSelection, Components
from pattren.models import LogosCategory, PresetLogos, UserLogo
from constructor.models import PrintingMethod
import json
from rest_framework.views import APIView
from api.email import send_register_email
from django.contrib.auth.mixins import LoginRequiredMixin

from pattren.models import LogosCategory, PresetLogos, UserLogo, PresetSublimationPatterns, SublimationCategory


# from api.utils.paginator import ResultsSetPagination


class ProductView(viewsets.ModelViewSet):
    queryset = models.ProductDesign.objects.all()
    serializer_classes = {
        'list': product_serializer.ProductDetailSerializer,
        'retrieve': product_serializer.ProductDetailSerializer,
    }
    default_serializer_class = product_serializer.ProductDetailSerializer

    # pagination_class = ResultsSetPagination

    # def get_queryset(self):
    #     import pdb; pdb.set_trace()
    #     return models.ProductDesign.objects.all()

    def get_serializer_class(self):
        product_design = self.get_object()
        # import pdb;
        # pdb.set_trace()
        if product_design.category.key == 'shirt':
            # serializer = product_serializer.ProductDetailSerializer(product_design)
            return self.serializer_classes.get(self.action, self.default_serializer_class)
            print('abc')
        if product_design.category.key == 'towel':
            # serializer = product_serializer.ProductDetailSerializer(product_design)
            return self.serializer_classes.get(self.action, self.default_serializer_class)
            print('abc')
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
    permission_classes = (IsAuthenticated,)
    queryset = UserLogo.objects.all()
    serializer_classes = {
        'list': logo_serializer.UserLogoListSerializer,
    }
    default_serializer_class = logo_serializer.UserLogoListSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], name='upload_logo', url_path='upload_logo')
    def upload_logo(self, request, *args, **kwargs):
        """
        Returns list of courses by country`.
        """

        try:
            file = request.data['file']
            obj = UserLogo(image=file, name=file.name, user=request.user)
            obj.save()
            serializer = self.get_serializer(UserLogo.objects.filter(user=request.user), many=True)
        except KeyError:
            raise ParseError("File is not Attached")

        return Response(serializer.data)


# class SublimationView(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     queryset = UserLogo.objects.all()
#     serializer_classes = {
#         'list': logo_serializer.UserSublimationListSerializer,
#     }
#     default_serializer_class = logo_serializer.UserSublimationListSerializer
#
#     # pagination_class = ResultsSetPagination
#
#     def get_serializer_class(self):
#         return self.serializer_classes.get(self.action, self.default_serializer_class)
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         queryset = queryset.filter(user=request.user)
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     # @action(detail=False, methods=['post'], name='upload_logo', url_path='upload_logo')
#     # def upload_logo(self, request, *args, **kwargs):
#     #     """
#     #     Returns list of courses by country`.
#     #     """
#     #
#     #     try:
#     #         file = request.data['file']
#     #         obj = UserLogo(image=file, name=file.name, user=request.user)
#     #         obj.save()
#     #         serializer = self.get_serializer(UserLogo.objects.filter(user=request.user), many=True)
#     #     except KeyError:
#     #         raise ParseError("File is not Attached")
#     #
#     #     return Response(serializer.data)


class LogoCategoryView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = LogosCategory.objects.all()
    serializer_classes = {
        'list': logo_serializer.LogoCategoryListSerializer,
        'retrieve': logo_serializer.LogoCategoryDetailSerializer,

    }
    default_serializer_class = logo_serializer.LogoCategoryListSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class SublimationCategoryView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = SublimationCategory.objects.all()
    serializer_classes = {
        'list': logo_serializer.SublimationCategoryListSerializer,
        'retrieve': logo_serializer.SublimationDetailSerializerWithCategory,
    }
    default_serializer_class = logo_serializer.SublimationCategoryListSerializer

    # pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    # @action(detail=False, methods=['post'], name='upload_logo', url_path='upload_logo')
    # def upload_logo(self, request, *args, **kwargs):
    #     """
    #     Returns list of courses by country`.
    #     """
    #
    #     try:
    #         file = request.data['file']
    #         obj = models.DesignImages(image=file, name=file.name)
    #         obj.save()
    #         serializer = self.get_serializer(models.DesignImages.objects.all(), many=True)
    #     except KeyError:
    #         raise ParseError("File is not Attached")
    #
    #     return Response(serializer.data)


class PriceList(APIView):
    permission_classes = (IsAuthenticated,)

    # IsAuthenticated
    def post(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        product_design = ProductDesign.objects.filter(pk=request.data.get("productId")).first()

        results = {'id': 1, 'name': product_design.name, 'price': 900, 'category': product_design.category.name,
                   'quantity': request.data.get("quantity")}

        dump = json.dumps(results)
        send_register_email(request.user.email, results)
        return HttpResponse(dump, content_type='application/json')


# class PriceView(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     queryset = PrintingMethod.objects.all()
#     serializer_classes = {
#         'list': product_serializer.ProductPriceDetailSerializer,
#         'retrieve': product_serializer.ProductPriceDetailSerializer,
#
#     }
#     default_serializer_class = product_serializer.ProductPriceDetailSerializer
#
#     # pagination_class = ResultsSetPagination
#
#     def get_serializer_class(self):
#         return self.serializer_classes.get(self.action, self.default_serializer_class)
#
#     @action(detail=False, methods=['get'], name='price', url_path='category/(?P<category_id>[0-9]+)/price')
#     def product_by_price(self, request, price, category_id, *args, **kwargs):
#         """
#          Returns list of componets  by country`.
#         """
#         qs = PrintingMethod.objects.filter(price=price).values_list('price', flat=True)
#         components = Components.objects.filter(id__in=list(qs))
#         serializer = self.get_serializer(components, many=True,
#                                          context={'category_id': category_id, 'request': request})
#         return Response(serializer.data)


class ComponentView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = ComponentSelection.objects.all()
    serializer_classes = {
        'list': component_serializer.ProductComponentListSerializer,
        'components_by_category': component_serializer.ProductComponentsListSerializer,
    }
    default_serializer_class = component_serializer.ProductComponentListSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=['get'], name='components', url_path='category/(?P<category_id>[0-9]+)/components')
    def components_by_category(self, request, category_id, *args, **kwargs):
        """
         Returns list of componets  by country`.
        """
        qs = ComponentSelection.objects.filter(category=category_id).values_list('component', flat=True)
        components = Components.objects.filter(id__in=list(qs))
        serializer = self.get_serializer(components, many=True,
                                         context={'category_id': category_id, 'request': request})
        return Response(serializer.data)


class ComponentCategoryView(viewsets.ModelViewSet):
    queryset = Components.objects.all()
    serializer_classes = {
        'list': component_serializer.ProductComponentCategoryNameListSerializer,
    }
    default_serializer_class = component_serializer.ProductComponentCategoryNameListSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=['get'], name='components', url_path='category')
    def components_by_category(self, request, category_id, name, *args, **kwargs):
        """
         Returns list of componets  by country`.
        """
        qs = Components.objects.filter(name=name).all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
