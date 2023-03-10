from django.urls import path
from . import views

urlpatterns = [
    path('', views.Show_Product.as_view(), name='home'),
    path('add/<int:product_id>', views.add_Product, name='add'),
    path('chosenlist/', views.Show_FinalChoose.as_view(), name='list'),
    path('payment/', views.Payment, name='payment'),
    path('back/', views.Back, name='back'), 
    path('delete/<int:Product_id>',views.Delete, name='delete')
]
