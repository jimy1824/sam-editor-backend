from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from api import views
from api.allviews import product

router = routers.DefaultRouter()
router.register(r'category', product.CategoryView)
router.register(r'product', product.ProductView)
router.register(r'user_logo', product.LogoView)
router.register(r'logos_category', product.LogoCategoryView)
router.register(r'component_selection', product.ComponentView)
router.register(r'component', product.ComponentCategoryView)


router.register(r'sublimation_category', product.SublimationCategoryView)


urlpatterns = [

    url(r'^', include(router.urls)),
    path('price', product.PriceList.as_view()),

]
