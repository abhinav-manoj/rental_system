from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms

# Create your models here.
# class Location(models.Model):
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)

#     def __str__(self):
#         return f'{self.city}, {self.state}, {self.country}'
# class Owner(models.Model):
#     name = models.CharField(max_length=225)

class HomeDetails(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='properties')
    # owner = models.CharField(max_length=225)
    property_type = models.TextField(null=True)
    location = models.TextField(null=True)
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=0)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    contact_number = models.CharField(max_length=20,  null=True,# Adjust based on your needs
        validators=[
            RegexValidator(
                
                regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    email_id = models.EmailField(max_length=254, null=True,unique=True) 
    square_footage = models.IntegerField()
    available_from = models.DateField()
    image = models.FileField( blank=True,null=True,upload_to='property_image/')
    
    def __str__(self):
        return self.owner




# class RentDetails(models.Model):
#     house = models.ForeignKey(HomeDetails,on_delete=models.CASCADE)
#     rental_date = models.DateField()
#     return_date = models.DateField()
    

# class Master(models.Model):
#     created_date = models.DateTimeField(auto_now_add=True)
#     isactive = models.BooleanField(default=True,verbose_name="Active")
#     created_user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)


    