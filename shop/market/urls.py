from django.urls import path

from . import views

app_name = "market"

urlpatterns = [
    path("item/<int:pk>/", views.item, name="item"),
]
