from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wellcome(Request):
    #return HttpResponse("<h1 style ='background:red'>hello all this is my first django app <h1>")
    my_dict={"insert_me":"i am coming from sub folder app1_home/reg..html"}
    return render(Request,"app1_home/Reg..html",context=my_dict)