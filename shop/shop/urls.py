from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("payment.urls", namespace="payment")),
    path("", include("market.urls", namespace="market")),
    path("admin/", admin.site.urls),
]
