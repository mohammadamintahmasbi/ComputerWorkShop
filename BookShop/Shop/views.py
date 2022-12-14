from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Chosen_Product
# Create your views here.

class Show_Product(TemplateView):
    template_name = 'Home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
   
        
        context.update({
            'products': Product.objects.all(),
        })

        return context


def add_Product(request, product_id):

    book = Product.objects.get(id=product_id)
    chosenBook = Chosen_Product.objects.create(Image=book.Image, name=book.name, author=book.author, description=book.description, cost=book.cost)
    messages.success(request, 'add successfully', 'success')

    return redirect('home')

class Show_FinalChoose(TemplateView):
    template_name = 'finallist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context.update({
            'chosen_products': Chosen_Product.objects.all(),
            
        })

        return context

def Payment(request):
    Chosen_Product.objects.all().delete()
    messages.success(request, 'Payment was successfully', 'success')
    return redirect('home')

def Back(request):
    messages.success(request, 'Return to main page', 'success')
    return redirect('home')

def Delete(request, Product_id):
    Chosen_Product.objects.get(id=Product_id).delete()
    messages.success(request, 'You delete your item', 'success')
    return redirect('list')