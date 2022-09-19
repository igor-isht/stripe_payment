import stripe
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from market.models import Item

from .models import ItemInCart, Order

stripe.api_key = "sk_test_51LjMpFE2KYKgRLYgaiXSirAFC5Dlh6mePHeRVdozkKPeYLwUHBaG3ky724Jmy5UgsNsCFvLrLvClinCBmWZNM0Vj002FE7bZR0"

DOMAIN = "http://127.0.0.1:8000"


class SuccessView(TemplateView):
    template_name = "payment/success.html"


class CancelView(TemplateView):
    template_name = "payment/cancel.html"


def buy(request, pk):
    order = Order.objects.get(buyer_id=pk)
    if order.discount:
        discounts = [
            {
                "coupon": "{{order.discount.coupon_id}}",
            }
        ]
    else:
        discounts = None

    positions = ItemInCart.objects.filter(order_id=order.id)
    line_items = []

    for position in positions:
        item = get_object_or_404(Item.objects, pk=position.item_id)
        line_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": item.price,
                },
                "adjustable_quantity": {
                    "enabled": True,
                    "minimum": 1,
                    "maximum": 10,
                },
                "quantity": 1,
            }
        )

    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        mode="payment",
        success_url=DOMAIN + "/success/",
        cancel_url=DOMAIN + "/cancel/",
        discounts=discounts,
    )

    return redirect(checkout_session.url, code=303)
