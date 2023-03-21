from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def index(request):
    return render(request , "index.html")

def search(request):
    if request.method == 'POST':  
        search = request.POST['search']
        url = "https://www.ask.com/web?q=freecodecamp"
    return render(request , "search.html")