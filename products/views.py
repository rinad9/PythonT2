from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# if there was request for url -> /pruducts 
# call this function -> index
def index (request):
    products = Product.objects.all()
    # calling render function with three arguments (request object, network template, 
    # dictionary that contains the data to be passed to the template)
    # this dictionary is called the context
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('new product')