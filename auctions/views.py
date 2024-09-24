from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import Listing,Bid,User,Watchlist,Comment
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Max,Min


from .models import User

# active listing page
def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html",
                  {'listings': listings}
                )


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
 
#creates a django form
class NewListingForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=500)
    url = forms.URLField(max_length=5000, required=False)
    startingbid = forms.IntegerField()
    Category = forms.CharField(max_length=50)


#utilises the form
def Create(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            startingbid = form.cleaned_data["startingbid"]
            url = form.cleaned_data["url"]
            Category = form.cleaned_data["Category"]
            
            # insert into respective database
            new_listing = Listing(title=title, description=description, startingbid=startingbid, url=url,Category=Category)
            new_listing.save()

            new_bid = Bid(Listing=new_listing, user=request.user,bid=startingbid)
            new_bid.save()
            
        else:
            return render(request, "auctions/createlisting.html", {"form": form})

    return render(request, "auctions/createlisting.html", {"form": NewListingForm()})

#to view the listing
def view(request,listing_id):

    #access the listing and getting id by clicking on it
    listing1 = get_object_or_404(Listing, id=listing_id)
    #When the bidding is too less too_less becomes true
    too_less = False
    if request.user.is_authenticated:
        current_user = request.user 
    #If I click on the remove from watchlist clicked becomes true    
    clicked = False
    
    #Save user activity to watchlist database
    if request.method == "POST":
        if not Watchlist.objects.filter(user=current_user, listing=listing1).exists():
            watchlist = Watchlist(user=current_user,listing=listing1)

            watchlist.save()
            
        else:    
            watchlist = Watchlist.objects.filter(user=current_user, listing=listing1) 
            watchlist.delete()
    #If listing's already in wishlist we would like to remove it when we click a button again.
    if request.user.is_authenticated:        
        if Watchlist.objects.filter(user=current_user, listing=listing1).exists():
            clicked = True
    #the lowest bid possible is accessed using this
    highest_bid_obj = Bid.objects.filter(Listing=listing1).aggregate(max_bid=Max('bid'))
    highest = highest_bid_obj['max_bid']
    
    #to post a higher bid
    if request.POST:
        if 'Bid' in request.POST:  
            higher_bid_amount = request.POST.get('higherBid')
            if int(higher_bid_amount)>int(highest):
                new_bid = Bid(bid=higher_bid_amount,user=request.user,Listing=listing1)  
                new_bid.save()  
                highest = higher_bid_amount
            else:
                too_less = True

    #When the close_listing button is not clicked            
    close_listing = False            
    #Check if the current user is the author of the listing
    bid1 = Bid.objects.filter(Listing_id=listing_id).order_by('bid').first()
    user1 = bid1.user
    if request.user ==  user1:
        close_listing = True   
    #If the user closes the listing
    if request.POST:
        if 'close' in request.POST:
            new = Listing.objects.get(id=listing_id)
            new.active = False
            new.save()
    
   #to comment on a listing
    if request.POST:
        if 'comments' in request.POST:      
            author = request.user
            comment =  request.POST.get('new')
            new_comment = Comment(author=author,listing=listing1,message=comment)
            new_comment.save()
    #retrive all comments        
    all_comments = Comment.objects.filter(listing=listing1)      

    #send all the variables to the template
    return render(request, "auctions/viewlisting.html",{
        "listing": listing1,
        "clicked": clicked,
        "highest": highest,
        "too_less": too_less,
        "close": close_listing,
        "comments": all_comments
    })

#to view all the closed listings 
def closed(request):
    lists = []
    message = False
    listings = Listing.objects.filter(active=False)

    #to see if the current user has won any auctions
    for listing in listings:
        bid1 = Bid.objects.filter(Listing_id=listing.id).order_by('bid').last()
        if request.user == bid1.user:
            message = True
            lists.append(listing.title)
    
    return render(request, "auctions/closed.html",
                  {'listings': listings,
                   "lists":lists,
                   "message" : message
                  })

# The watchlist 
def watch(request):
    current_user = request.user
    watchlist = Watchlist.objects.filter(user=current_user)
    listings = [item.listing for item in watchlist]
    return render(request, "auctions/watchlist.html",
                  {'listings': listings}
                )

#all the categories in a bullet point
def Categories(request):
    all = Listing.objects.all()
    
    category = [items.Category for items in all]
    category1 = list(set(category))
    return render(request, "auctions/categories.html",
                  {'items': category1}
                )


#display all of the listing with the applicable categories when clicked
def displayCategory(request,category):
    listings = Listing.objects.filter(Category=category)
        
    return render(request, "auctions/index.html",
                  {'listings': listings}
                )

