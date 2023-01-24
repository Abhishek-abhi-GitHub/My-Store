from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


class Products(models.Model):

    name=models.CharField(max_length=999)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=999)
    category=models.CharField(max_length=999)
    image=models.ImageField(null=True,upload_to="images")

    @property
    def avg_rating(self):
        ratings=self.reviews_set.all().values_list("rating",flat=True)
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0
    @property
    def number_rating(self):
        num=self.reviews_set.all().values_list("rating",flat=True)
        if num:
            return len(num)
        else:
            return 0

    def __str__(self):
        return self.name

class Carts(models.Model):

    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    options=(
        ("order-placed","order-placed"),
        ("in-cart","in-cart"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")



class Reviews(models.Model):

    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=500)

    def __str__(self):
        return self.comment


# ORM
# orm for creating a resouece
# modelname.object.create(field1=value1,field2=value2....)


class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("despatched","despatched"),
        ("in-transit","in-transit"),
        ("canceled","canceled"),
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=25)