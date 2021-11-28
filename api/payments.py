from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
import stripe
from constructor.models import UserOrder

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutView(APIView):
    def post(self, request):
        # import pdb;pdb.set_trace()
        # try:
        #     print(request.data.get('order_no'))
            if not UserOrder.objects.filter(order_no=request.data.get('order_no')).exists():
                return Response({'error': 'order no not found'}, status=status.HTTP_400_BAD_REQUEST)
            order = UserOrder.objects.get(order_no=request.data.get('order_no'))
            product = stripe.Product.create(
                name=order.order_no,
            )
            # print(product)
            price = stripe.Price.create(
                product=product.id,
                unit_amount=int(order.total_price)*100,
                currency='usd',
            )
            # print(price)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card', ],
                mode='payment',
                success_url=settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '/?canceled=true',
            )
            print(checkout_session)
            return Response(checkout_session)
        # except:
        #     return Response(
        #         {'error': 'Something went wrong when creating stripe checkout session'},
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #     )
