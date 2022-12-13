from django.shortcuts import render
from .models import Product
# Create your views here.
def Show_Product(request):
    all = Product.objects.all()
    return render(request, 'Home.html', {'products':all})
