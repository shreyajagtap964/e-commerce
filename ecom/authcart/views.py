from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Passward is Not Matching")
            return render(request,'signup.html')
            
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email already exist")
                # return redirect('/signup.html')
            return render(request,'signup.html')

        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email,email,password)        
        user.save() 
        messages.warning(request,"User created")       
    return render(request,'signup.html')


def handlelogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid credentials")
            return redirect('/auth/login')

    return render(request,"login.html")


def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')

