from django.contrib.auth import authenticate, login, logout, forms
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import datetime
from .models import User, AuctionListing, Bid, Comment
from django.contrib import messages


def index(request):
    if request.method == "GET":
        category = request.GET.get('category')
        if category:
            auction_listings = AuctionListing.objects.filter(category=category)
        else:
            auction_listings = AuctionListing.objects.all()

        # Compactando os dados usando zip
        ids = [listing.id for listing in auction_listings]
        titles = [listing.title for listing in auction_listings]
        descriptions = [listing.description for listing in auction_listings]
        current_prices = [listing.current_price for listing in auction_listings]
        owners = [listing.owner for listing in auction_listings]
        categories = [listing.category for listing in auction_listings]
        status = [listing.active for listing in auction_listings]
        images = [listing.image for listing in auction_listings]
        winners = [listing.winner for listing in auction_listings]

        # Usando zip para compactar os dados
        zipped_data = zip(ids, titles, descriptions, current_prices, categories, images, owners, status, winners)

        # Criando a lista de dicionários
        items = [
            {
                "id": item_id,
                "title": title,
                "description": description,
                "current_price": current_price,
                "category": category,
                "image": image,
                "owner": owner,
                "status": status,
                "winner": winner if winner else "No winner yet",
            }
            for item_id, title, description, current_price, category, image , owner, status, winner in zipped_data
        ]

        return render(request, "auctions/active_auctions.html", {
            'items': items,
            "user": request.user, 
            })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


from django.core.files.base import ContentFile

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            if 'image_upload' in request.FILES:
                user.image_blob = request.FILES['image_upload'].read()
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_auction(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_price = request.POST["starting_price"]
        starting_price = float(starting_price.replace(',', '.'))
        image = request.POST["image"]
        category = request.POST["category"]

        AuctionListing.objects.create(
            title=title,
            description=description,
            starting_price=starting_price,
            current_price= 0,
            category=category,
            image=image,
            owner=request.user,
        )

        return redirect("index")

    return render(request, "auctions/create_auction.html")



def watchlist(request):
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    return render(request, "auctions/watchlist.html",
        {
        'items': listings,
    })



def show(request, id):
    item = get_object_or_404(AuctionListing, id=id)
    favorito = request.user in item.watchlist.all()
    comments = Comment.objects.filter(auction=item)

    return render(request, "auctions/show.html",{
        'favorito' : favorito,
        'item':item,
        'comments':comments,
    })

def removeWatchList(request, id):
    watchlistData = AuctionListing.objects.get(id=id)
    currentUser = request.user
    watchlistData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse('show' , args = (id, ))) 


def addWatchList(request, id):
    watchlistData = AuctionListing.objects.get(id=id)
    currentUser = request.user
    watchlistData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse('show' , args = (id, ))) 

def doBide(request, id):

    if request.method == "POST":
        bid = Bid.objects.all()
        auction = AuctionListing.objects.get(id=id)
        bidder = request.user
        startPrice = auction.starting_price
        currentPrice = auction.current_price
        newBid = float(request.POST["newBid"])

    if newBid > startPrice and newBid > currentPrice and request.method == "POST" :
        actualBid = Bid.objects.create(
        auction = auction,
        amount=newBid,
        bidder=bidder,
        bid_time=datetime.now()
        )

        auction.current_price = newBid
        auction.last_bid = actualBid
        auction.save()
        messages.success(request, 'Bid placed successfully.')


    elif newBid < startPrice or newBid < currentPrice:
        messages.error(request, 'Bid was not successful.')

    return HttpResponseRedirect(reverse('show', args=(id,)))   


def closeAuction(request, id):
    if request.method == "POST":
        auction = AuctionListing.objects.get(id=id)
        auction.active = False
        if auction.current_price == 0:
            auction.winner = auction.owner
        else:
            auction.winner = auction.last_bid.bidder

        auction.save()
        
    return HttpResponseRedirect(reverse('index'))
    
    
def serve_image(request, user_id):
    user = User.objects.get(id=user_id)
    return HttpResponse(user.image_blob, content_type='image/jpeg')


def comment(request, id):
    if request.method == "POST":

        auction = AuctionListing.objects.get(id=id)
        commenter = request.user
        text = request.POST["textComment"]

        comment = Comment.objects.create(
            auction = auction,
            commenter = commenter,
            text = text
        )

        comment.save()
    
    comment = Comment.objects.all()
    return HttpResponseRedirect(reverse('show', args=(id,)))



def categories(request):

    distinct_categories = AuctionListing.objects.values('category').distinct()
    return render(request, "auctions/categories.html", {
        'categories': distinct_categories
        })
