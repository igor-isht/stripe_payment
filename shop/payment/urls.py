from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('buy/<int:pk>/', views.buy, name='buy'),
]