from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Location(models.Model):
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)

#     def __str__(self):
#         return f'{self.city}, {self.state}, {self.country}'

class HomeDetails(models.Model):
    owner = models.CharField(max_length=225)
    # location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='location')
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    available_from = models.DateField()
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

# class RentDetails(models.Model):
#     house = models.ForeignKey(HomeDetails,on_delete=models.CASCADE)
#     rental_date = models.DateField()
#     return_date = models.DateField()
    

class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True,verbose_name="Active")
    created_user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

class State(Master):
    State_name=models.CharField(max_length=200,verbose_name='State Name')