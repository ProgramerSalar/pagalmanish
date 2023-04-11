from django.shortcuts import render
from django.http import HttpResponse 
from . models import Product
from math import ceil

# Create your views here.
def index(request):
    products  = Product.objects.all()
    n = len(products)
    nnSlides = n//4 + ceil((n/4) + (n//4))
    params = {'no_of_slides': nnSlides , 'range': range(1, nnSlides) , 'product': products}
    return render(request , 'shop/index.html', params)

def about(request):
    return render(request , 'shop/about.html')


def contact(request):
    return HttpResponse('contact page')


def tracker(request):
    return HttpResponse('tracker  page')

def search(request):
    return HttpResponse('search page')


def productview(request):
    return HttpResponse('product view page')



def checkout(request):
    return HttpResponse('checkout page')
