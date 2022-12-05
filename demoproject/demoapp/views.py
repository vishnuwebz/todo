from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Programmers
from .models import Languages,Languagesbg

# Create your views here.

# def demo(request):
#     return HttpResponse("Hey There,Welcome To My Django World!")
# def home(request):
#     return HttpResponse("Hey,Welcome to Home Page")
# def about (request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("This is Contact from 'HttpResponse'")
# def detail(request):
#     return render(request,"detail.html")
# def thanks(request):
#     return HttpResponse("Thankyou For Visiting From HttpResponse")


'''def form(request):
    return render(request,"entryform.html")
def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    div=x/y
    mul=x*y
    add=x+y
    sub=x-y

    return render(request,"operations.html",{'division':div,'multiplication':mul,'addition':add,'subtraction':sub})
    '''
def giants(request):
    obj=Programmers.objects.all()
    obj1 = Languages.objects.all()
    obj2 = Languagesbg.objects.all()
    return render(request,"index.html",{'programmer':obj,'language':obj1,'lbackground':obj2})

'''def langs(request):
    
    return render(request,"index.html",{'language':obj1})

def lbg(request):
    obj2=Languagesbg.objects.all()
    return render(request,"index.html",{'lbackground':obj2})
'''
def register(request):
    #fetching datas from users
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['emailID']
        password=request.POST['password']
        cpassword=request.POST['password1']

        #if both passwords are same then only user can be saved
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"mailid already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                messages.info(request,"user created successfully")
                user.save();
                print("user created")
                return redirect('login')


                # print("incorrect password")
        else:
            messages.info(request,"password not matched")
            return redirect('register')

        return redirect("/")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')


    return render(request,"login.html")

#logout
def logout(request):
    auth.logout(request)
    return redirect("/")

