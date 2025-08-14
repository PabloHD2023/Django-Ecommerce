class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exists

        cart = self.session.get('session_key')

        #If the user is new
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        # Make sure cart is available on all pages of the site
        self.cart = cart

    def add (self, product):
        product_id = str(product.id)
        #Logic
        if product_id in self.cart: #IF product already in cart
            pass # Do nothing, or update quantity if needed
        #If product not in cart, add it
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True

