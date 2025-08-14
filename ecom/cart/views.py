from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def cart_add(request):
    #Get the cart
    cart = Cart(request)
    #Test for post
    if request.POST.get('action') == 'post':
        #Get the product id
        product_id = int(request.POST.get('product_id'))
        #Look up the product in DB
        product = get_object_or_404(Product, id=product_id)
        #Add the product to the cart
        cart.add(product=product)
        #Return a JsonResponse
        response = JsonResponse({'Product Name: ': product.name, 'Product Price: ': product.price})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass

