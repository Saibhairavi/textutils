"""iCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import this
from django.contrib import admin
from django.urls import path,include

# this is how django admin panel changed to specific app's  admin 
# change the header of the admin panel. instead of django admin
admin.site.site_header="iCoder Admin" 
#to change the title of admin panel
admin.site.site_title='iCoder Admin Panel'
admin.site.index_title="Welcome to iCoder Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('blog.urls'))
]
