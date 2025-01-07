from django.urls import path,include
# from first_app.views import home
from .import views
urlpatterns = [
   
    path('',views.home),
]