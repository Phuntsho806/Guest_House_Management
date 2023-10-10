from django.shortcuts import render


# Create your views here.
def home_view(request):
  return render(request, 'Home.html')
    
def room_book_view(request):
  return render(request, 'roombook.html')    

def food_view(request):
  return render(request, 'Fooding.html')

def about_us_view(request):
  return render(request, 'AboutUs.html')

def login_view(request):
  return render(request, 'login.html')

def signup_view(request):
  return render(request, 'signup.html')