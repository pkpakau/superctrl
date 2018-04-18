from django.db import models

# Create your models here.
class Order(models.Model):
    orderid=models.CharField(max_length=10)
    placedby=models.CharField(max_length=100)
    address=models.TextField()
    contact=models.IntegerField()
    quantity=models.IntegerField()
    delivery_date=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.orderid

class Product(models.Model):
    order=models.ForeignKey(Order,null=True,blank=True)
    productid=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    stock=models.IntegerField()
    image=models.FileField(upload_to='product_images')

    def __str__(self):
        return self.name+"-"+self.productid