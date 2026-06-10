from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        "userName": "ASUS",
        "post_count":1,"posts": [
            "Learning Django",
            "Python is awesome",
            "My first website"
        ]
    }

    return render(request, 'blog/home.html',context)

# Create your views here.
def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")