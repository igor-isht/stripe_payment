from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('payment.urls', namespace='payment')),
    path('', include('market.urls', namespace='market')),
    path('admin/', admin.site.urls),
]
