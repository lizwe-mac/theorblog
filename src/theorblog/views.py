from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    user = request.user
    if request.user.is_authenticated:
        greeting = "Hey, {}. Checkout the requirements:".format(user)
        context = {"my_greeting": greeting, "my_list": ["Python3", "Django 2.2", "MySQL", "Heroku"]}
    else:
        greeting = "Hey, {}. Please sign up for awesome content!".format(user)
        context = {"my_greeting": greeting, "my_list": ["Python3", "Django 2.2", "MySQL", "Heroku"]}
    return render(request, "home.html", context)

def about_page(request):
    user3 = request.user
    return render(request, "about.html", {"user": user3})
    #return HttpResponse("<h1>ABOUT THE APP</h1>")

def contact_page(request):
    user = request.user
    return render(request, "contact.html", {"user": user})
    #return HttpResponse("<h1>PLEASE CONTACT US</h1>")    