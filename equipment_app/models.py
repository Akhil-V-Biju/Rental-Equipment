from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Add_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to='imagefile/',null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url






class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description =models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='equipment_images/')
    quantity = models.IntegerField(null=True,blank=True)
    priceday= models.IntegerField(null=True,blank=True)
    pricehour= models.IntegerField(null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    



class Buy_cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    equipment= models.ForeignKey(Equipment,on_delete=models.CASCADE, default=1)
    ndate=models.DateField(null=True,blank=True)
    nhours=models.IntegerField(null=True,blank=True)
    ndays=models.IntegerField(null=True,blank=True)
    prof=models.ImageField( upload_to='product_image/',null=True,blank=True)
    bookstatus=models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            url = self.prof.url
        except:
            url = ''
        return url




class Testi(models.Model):
    user=models.ForeignKey(Add_profile, on_delete=models.CASCADE,null=True,blank=True)
    text=models.TextField(null=True,blank=True)  


    @property
    def imageURL(self):
        try:
            url=self.user.image.url
        except:
            url=''
        return url

    








