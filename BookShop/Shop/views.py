from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Product
# Create your views here.

class Show_Product(TemplateView):
    template_name = 'Home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
   
        
        context.update({
            'products': Product.objects.all(),
        })

        return context
