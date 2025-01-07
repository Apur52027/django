from django.shortcuts import render
import datetime
def home(request):
  d={'author':'Rahim','age':5,'lst':['python','c++','java','c'],'birthday':datetime.datetime.now(),
    'course':[
      {
      'id':1,
      'name':'C++',
      'fee' :5000,
     
     },

    {
      'id':2,
      'name':'C',
      'fee' :500,
    },
    {
      'id':3,
      'name':'Django',
      'fee' :5000,
    },
    ]}
  return render(request,'home.html',context=d)
