from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home,name="home"),
    path('contact', views.contact,name="contact"),
    path('about', views.about,name="about"),
    path('search',views.search,name="search"),
    path('signup',views.signup,name="signup"),
    path('login_user',views.login_user,name='login'),
    path('logout_user',views.logout_user,name='logout')

    #endpoints,methodname
]

