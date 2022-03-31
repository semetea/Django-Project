from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
def index(request) :
    return render(request, 'acc/index.html')

def login_user(request) :
    if request.method == 'POST' :
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        user = authenticate(username=un, password=up)
        if user :
            login(request, user)
            return redirect('acc:index')
        else :
            pass # 마지막날
    return render(request, "acc/login.html")

def logout_user(request) :
    logout(request)
    return redirect("acc:login")

def signup(request) :
    if request.method == 'POST' :
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucom")
        upic = request.FILES.get("upic")
        User.objects.create_user(username=un, password=up, comment=uc,pic=upic)
        return redirect('acc:login')
        
    return render(request, "acc/signup.html")

def profile(request) :
    return render(request, 'acc/profile.html')

def delete(request) :
    u = request.user
    ck = request.POST.get("pwcheck")
    if(check_password(ck,u.password)) :
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else :
        pass
        return redirect("acc:profile")

    return redirect("acc:index")

def update(request) :
    if request.method == 'POST' :
        u = request.user
        up = request.POST.get('upass')
        uc = request.POST.get('ucom')
        upic = request.FILES.get('upic')
        if up :
            u.set_password(up)
        u.comment = uc
        u.pic.delete()
        u.pic = upic
        u.save()
        login(request, u)
        return redirect("acc:profile")
    return render(request, "acc/update.html")
