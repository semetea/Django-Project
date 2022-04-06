from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages

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
            messages.success(request, f"WELCOME {user}")
            return redirect('acc:index')
        else :
            messages.error(request, "계정정보가 일치하지 않습니다!")
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
        try:
            User.objects.create_user(username=un, password=up,
            comment=uc, pic=upic)
            return redirect("acc:login")
        except:
            messages.error(request, "중복된 계정이 있습니다")
    return render(request, 'acc/signup.html')

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
        messages.info(request, "패스워드가 일치하지 않아 삭제되지 않았습니다")
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
