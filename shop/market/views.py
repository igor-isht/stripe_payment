from locale import currency
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.views import View
import stripe

from .models import Item

stripe.api_key = 'sk_test_51LjMpFE2KYKgRLYgaiXSirAFC5Dlh6mePHeRVdozkKPeYLwUHBaG3ky724Jmy5UgsNsCFvLrLvClinCBmWZNM0Vj002FE7bZR0'

DOMAIN = 'http://127.0.0.1:8000'

def item(request, pk):
    item = get_object_or_404(Item.objects, pk=pk)
    template = 'market/item_detail.html'
    price = format(item.price/100, '.2f')
    context = {
        'item': item,
        'price': price,
    }
    return render(request, template, context)

