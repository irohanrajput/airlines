from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def index_users(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index_users"))
        else:
            return render(request, "users/login.html", {"message": "invalid credentidals"})
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/logout.html", {"message": "Logged out Successfully"
                                                })

def signup_view(request):
    return render(request, "users/signup.html")

def flight_redr_view(requset):
    return HttpResponseRedirect(reverse("index"))