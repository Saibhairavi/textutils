from http.client import HTTPResponse
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
    return render(request, 'home/home.html', {})

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        content=request.POST.get('content')
        contact=Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            # messages.error(request, "Please fill the form correctly")
            messages.add_message(request, messages.ERROR,"Please fill the form correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.add_message(request,messages.SUCCESS,"Your message has been successfully sent")
            
    return render(request, 'home/contact.html', {})


def about(request):
    return render(request, 'home/about.html', {})


def search(request):    
    query=request.GET['query']
    
    if len(query)>70:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor=Post.objects.filter(author__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPostsSlug=Post.objects.filter(slug__icontains=query)
        allPosts=allPostsTitle.union(allPostsAuthor,allPostsContent,allPostsSlug)
    if allPosts.count==0:
        messages.warning(request,"No search results found. Please refine your query.")
    
    params={'allPosts': allPosts,'query':query}
    return render(request, 'home/search.html', params)


def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        lname=request.POST.get('lname')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request,'Please confirm your password')
            return redirect('home')
        if not username.isalnum():
            messages.error(request,'Username consists of numers and characters')
            return redirect('home')

        new_user=User.objects.create_user(username,email,pass1)
        new_user.first_name= fname
        new_user.last_name= lname
        new_user.save()
        messages.success(request,'User created Successfully!!')
        return redirect('home')
    else:
        return HttpResponse("error")


def login_user(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['pass']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'login Succesful')
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials .Please try again")
            return redirect('home')
    return HttpResponse("Login")

    
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')