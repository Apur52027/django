
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('authors/',include('author.urls')),
    path('profile/',include('profiles.urls')),
    path('post/',include('posts.urls')),
    path('category/', include('categories.urls')),
    
]
