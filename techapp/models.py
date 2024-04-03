from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class laptop(models.Model):
    Name=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    colour=models.CharField(max_length=30)
    details=models.CharField(max_length=3000)
    price=models.IntegerField()
    la_image=models.ImageField(upload_to='image',default='')
    la_image1=models.ImageField(upload_to='image',default='')
    la_image2=models.ImageField(upload_to='image',default='')

class Cart(models.Model):
    pid=models.ForeignKey(laptop,on_delete=models.CASCADE,db_column='pid')
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    quantity=models.IntegerField(default=1)

class Order(models.Model):
    orderid=models.IntegerField()
    pid=models.ForeignKey(laptop,on_delete=models.CASCADE,db_column='pid')
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    quantity=models.IntegerField()

class Billingdetails(models.Model):
    F_name=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    
