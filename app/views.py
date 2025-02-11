from django.shortcuts import render
from .forms import userForm
# Create your views here.
def home(request):
  form = userForm()
  return render(request,'home.html',{'form' :form})