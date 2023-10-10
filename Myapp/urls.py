from django.urls import path
from Myapp import views

urlpatterns = [
  path('Home.html', views.home_view, name='home'),
  path('roombook.html', views.room_book_view, name='bookroom'),
  path('Fooding.html', views.food_view, name='food'),
  path('AboutUs.html', views.about_us_view, name='Contact'),
  path('login.html', views.login_view, name='login'),
  path('signup.html', views.signup_view, name='signup'),
]
