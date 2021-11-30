from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from api import views
from api.allviews import product
from .user import UserProfileUpdateView, UserProfileView
from .payments import StripeCheckoutView
from api.allviews.product import OrdersView, OrderDeleteView

router = routers.DefaultRouter()
router.register(r'category', product.CategoryView)
router.register(r'product', product.ProductView)
router.register(r'user_logo', product.LogoView)
router.register(r'logos_category', product.LogoCategoryView)
router.register(r'component_selection', product.ComponentView)
router.register(r'component', product.ComponentCategoryView)
router.register(r'printing_method', product.PriceView)

router.register(r'sublimation_category', product.SublimationCategoryView)

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^send_invoice/', product.SendInvoiceView.as_view(), name="send_invoice"),
    url(r'^update_profile/', UserProfileUpdateView.as_view(), name="update_profile"),
    url(r'^get_profile/', UserProfileView.as_view(), name="get_profile"),
    url(r'^create-checkout-session/', StripeCheckoutView.as_view()),
    url(r'^orders/', OrdersView.as_view()),
    path('order_delete/<str:order_no>', OrderDeleteView.as_view(), name='order_delete'),

]
