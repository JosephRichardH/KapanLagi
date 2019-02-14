from django.db import models
from django.db.models import CharField
from django.shortcuts import render,redirect
from .models import Lagu
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
<<<<<<< HEAD
def LaguPost(request):
    return render(request, 'Contoh0.html', {})

def LirikLagu(request):
    KumpulanLagu = Lagu.objects.all()
    return render(request, 'Lirik.html', {'KumpulanLagu' : KumpulanLagu})

#def Lagu_Input(request):
#    if request.method == "POST":
#        form = PostForm(request.POST, request.FILES)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#            return redirect(LaguPost)
#    else:
#        form = PostForm()
#        return render(request, 'LaguInput.html', {'form': form})
#
def LaguDetail(request, lagu_id):
    satu_lagu = Lagu.objects.get(pk=lagu_id)
    return render(request, 'LaguDetail.html', {'Lagus': satu_lagu})

def PrintDetail(request, lagu_id):
    satu_lagu = Lagu.objects.get(pk=lagu_id)
    return render(request, 'print.html', {'Lagus': satu_lagu})
=======
def Lagu_Post(request):
    #Lagus = Lagu.objects.all()
    return render(request, 'Contoh0.html', {})

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
#
#def Lagu_Detail(request, barang_id):
#    Lagus = Lagu.objects.get(pk=barang_id)
#    return render(request, 'LaguDetail.html', {'Lagus':Lagu})

def Lagu_Signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
    else:
        form=UserCreationForm()
    return render(request,'LaguSignup.html',{'form':form})

def Lagu_Signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect (Lagu_Post)
    else:
        form=AuthenticationForm()
    return render(request,'LaguSignin.html',{'form':form})

def Lagu_Signout(request):
    if request.method == "POST":
        
        logout(request)
        
        return redirect (Lagu_Post)
>>>>>>> fe74e940c5922f119aa55b5c76a9417ffc8639f9
