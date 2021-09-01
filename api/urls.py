from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from api import views
from api.allviews import product

router = routers.DefaultRouter()
router.register(r'category', product.CategoryView)
router.register(r'product', product.ProductView)
router.register(r'logos', product.LogoView)
router.register(r'logos_category', product.LogoCategoryView)

urlpatterns = [

    url(r'^', include(router.urls)),

]
