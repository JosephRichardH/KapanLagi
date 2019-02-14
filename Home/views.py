from django.shortcuts import render
from django.db import models
from django.db.models import CharField

from django.shortcuts import render,redirect
from .models import Lagu
from .forms import PostForm

# Create your views here.
def BarangPost(request):
    Lagus = Lagu.objects.all()
    return render(request, 'Lagu.html', {'Lagus':Lagus})

def Lagu_Input(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(LaguPost)
    else:
        form = PostForm()
        return render(request, 'LaguInput.html', {'form': form})

def Lagu_Detail(request, barang_id):
    Lagus = Lagu.objects.get(pk=barang_id)
    return render(request, 'LaguDetail.html', {'Lagus':Lagu})
