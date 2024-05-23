from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import User, Post
from django.core.paginator import Paginator

from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.all().order_by('-timestamp')

    # Create a Paginator object
    paginator = Paginator(posts, 10)  # Show 10 posts per page

    # Get the page number from the GET parameters
    page_number = request.GET.get('page')

    # Get the posts for the current page
    posts = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "posts": posts
    })


# AUTH VIEWS

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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })
        
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")




# POST VIEWS


def create_post(request):
    if request.method == "POST":
        content = request.POST["content"]

        post = Post(
            owner=request.user, 
            content=content,
            image=request.FILES["image"] if "image" in request.FILES else None)

        post.save()

        return JsonResponse({"success": True})


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return JsonResponse({"success": True})


def edit_post(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":
        post.content = request.POST["content"]
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        
        post.owner = request.user
        post.save()
        return redirect('index')
    else:
        return JsonResponse({"content": post.content})


def do_like(request, id):
    post = get_object_or_404(Post, id=id)
    liked = False
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    like_count = post.likes.count()
    return JsonResponse({'liked': liked, 'like_count': like_count})


def user_profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(owner=user).order_by('-timestamp')

    # Create a Paginator object
    paginator = Paginator(posts, 10)  # Show 10 posts per page

    # Get the page number from the GET parameters
    page_number = request.GET.get('page')

    # Get the posts for the current page
    posts = paginator.get_page(page_number)

    current_profile = User.objects.get(username=username)
    return render(request, "network/profile.html", {
        "posts": posts,
        "current_profile": current_profile
    })

def update_profile(request, username):
    user = User.objects.get(username=username)

    if request.method == "POST":
        profile_picture = request.FILES.get("profile_picture")
        background_picture = request.FILES.get("background_picture")

        if profile_picture is not None:
            user.profile_picture = profile_picture

        if background_picture is not None:
            user.background_picture = background_picture

        user.save()

    return redirect('profile', username=username)



def follow(request, id):
    user = get_object_or_404(User, id=id)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
        following = False
    else:
        user.followers.add(request.user)
        following = True
    followers_count = user.followers.count()
    return JsonResponse({"following": following, "followers_count": followers_count})


def followingPage(request):
    user = User.objects.get(username=request.user)
    following = user.following.all()
    posts = Post.objects.filter(owner__in=following).order_by('-timestamp')

    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')

    posts = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "posts": posts
    })