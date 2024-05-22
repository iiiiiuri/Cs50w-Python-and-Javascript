from django.db import models
from django.contrib.auth.models import AbstractUser
import base64

class User(AbstractUser):
    image_blob = models.BinaryField(null=True, blank=True)

    def image_base64(self):
        return base64.b64encode(self.image_blob).decode('utf-8'), self.username.capitalize()

    
class AuctionListing(models.Model):
    title = models.CharField(max_length=26)
    description = models.CharField(max_length=1050)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    category = models.CharField(max_length=25, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name='listingWatchlist')
    last_bid = models.ForeignKey('Bid', on_delete=models.SET_NULL,blank=True ,null=True, related_name='last_bid')    
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True ,null=True, related_name='winner')

    def __str__(self):
        return self.title



class Bid(models.Model):
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name= 'bids')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField()

    def __str__(self):
        return f'Bid on {self.auction.title} by {self.bidder.username}'
    

class Comment(models.Model):
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name= 'comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Comment on {self.auction.title} by {self.commenter.username}'