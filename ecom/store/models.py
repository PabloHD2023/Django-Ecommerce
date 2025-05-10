from django.db import models
import datetime

# Create your models here.

#Category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    #Customizing the admin panel so that it shows the plural name of the model
    class Meta:
        verbose_name_plural = "Categories"

#Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

#Product model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=250, blank=True, null=True, default="")
    image = models.ImageField(upload_to='uploads/products/')
    #Agregamos un mensaje si el producto está en oferta
    offer = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    #Agregamos un mensaje si el producto está en stock
    #stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
#Order model
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.TextField(max_length=250, blank=True, null=True, default="")
    phone=models.CharField(max_length=15, blank=True, null=True, default="")
    order_date=models.DateTimeField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product

