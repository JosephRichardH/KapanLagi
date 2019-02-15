from django.db import models
from django.db.models import CharField, Q
from django.shortcuts import render,redirect
from .models import Lagu
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def Tampilan_Home(request):
    return render(request, 'Contoh0.html', {})


def Lagu_SignUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
    else:
        form=UserCreationForm()
    return render(request,'LaguSignUp.html',{'form':form})

def Lagu_SignIn(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect (request.POST.get('next'))
            else: 
                return redirect (Lagu_Post)
    else:
        form=AuthenticationForm()
    return render(request,'LaguSignIn.html',{'form':form})

def Lagu_Signout(request):
    if request.method == "POST":
        
        logout(request)
        
        return redirect (Lagu_Post)

@login_required(login_url=Lagu_SignIn)
def Lagu_Input(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(Lagu_Post)
    else:
        form = PostForm()
        return render(request, 'LaguInput.html', {'form': form})


def LaguDetail(request, lagu_id):
    satu_lagu = Lagu.objects.get(pk=lagu_id)
    return render(request, 'LaguDetail.html', {'Lagus': satu_lagu})

@login_required(login_url=Lagu_SignIn)
def PrintDetail(request, lagu_id):
    satu_lagu = Lagu.objects.get(pk=lagu_id)
    return render(request, 'print.html', {'Lagus': satu_lagu})

def LirikLagu(request):
    satu_lagu = Lagu.objects.all()
    query = request.GET.get("query")
    if query:
        queryset_list=Lagu.filter(
            Q(judul_icontains=query)|
            Q(artis_icontains=query)|
            Q(teks_icontains=query)
            ).distinct()
    else:
        queryset_list=""
    return render(request, 'Lirik.html', {'Lagus': satu_lagu}, {'queries':queryset_list})
