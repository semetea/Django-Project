from django.shortcuts import render, redirect
from .models import Topic, Sel
from django.core.paginator import Paginator

# Create your views here.
def index(request) :
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(request, "vote/index.html", context)

def detail(request, tpk) :
    t = Topic.objects.get(id=tpk)
    s = t.sel_set.all()
    context = {
        "t" : t,
        "sset" : s
    }
    return render(request, "vote/detail.html", context)

def vote(request, tpk) :
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all() :
        t.voter.add(request.user)
        spk = request.POST.get("sel")
        s = Sel.objects.get(id=spk)
        s.choicer.add(request.user)
    
    return redirect("vote:detail", tpk)
    
def cancel(request, tpk) :
    t = Topic.objects.get(id=tpk)
    t.voter.remove(request.user)
    # 역참조를 이용해 찾아내기(for문 쓰는 것보다 빠르다)
    # t.sel_set.get(choicer=request.user).choicer.remove(request.user)
    request.user.sel_set.get(topic=t).choicer.remove(request.user)

    return redirect("vote:detail", tpk)

def create(request) :
    if request.method == 'POST' :
        top = request.POST.get("top")
        c = request.POST.get("con")
        sn = request.POST.getlist("sname")
        sc = request.POST.getlist("scon")
        sp = request.FILES.getlist("spic")
        t = Topic(subject=top, content=c, maker=request.user)
        t.save()
        print(sn,sc,sp)

        for name, con, pic in zip(sn,sc,sp) :
            Sel(topic=t, sname=name, spic=pic, scon=con).save()
        return redirect("vote:index")

    return render(request, "vote/create.html")

def delete(request, tpk) :
    t = Topic.objects.get(id=tpk)
    if t.maker == request.user :
        s = t.sel_set.all()
        for i in s :
            i.spic.delete()
        t.delete()
    else :
        pass # 마지막
    return redirect("vote:index")