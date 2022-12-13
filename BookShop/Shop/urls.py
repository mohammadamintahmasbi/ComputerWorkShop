from django.urls import path
from . import views

urlpatterns = [
    path('', views.Show_Product.as_view(), name='home')
]
