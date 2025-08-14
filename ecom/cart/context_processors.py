from .cart import Cart

#Create a context processor to make the cart available in all templates
def cart(request):
    #Return the default data from our Cart class
    return {'cart': Cart(request)}