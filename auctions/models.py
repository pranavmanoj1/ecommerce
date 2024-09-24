from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass  

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName





class Listing(models.Model):
    title = models.CharField(max_length=50)
    Category = models.CharField(max_length=50, default="appliances")
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=5000, blank=True, null=True)
    startingbid = models.IntegerField(max_length=50)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlists')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name='watchlists')

    




class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='userComment')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name='listingComment')
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"

class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='userBid')
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="Listing")



