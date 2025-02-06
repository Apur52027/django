
from django.contrib import admin
from django.urls import path,include
# from .import views
from first_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
]
