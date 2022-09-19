from locale import currency

import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.base import TemplateView

from .models import Item


def item(request, pk):
    item = get_object_or_404(Item.objects, pk=pk)
    template = "market/item_detail.html"
    price = format(item.price / 100, ".2f")
    context = {
        "item": item,
        "price": price,
    }
    return render(request, template, context)
