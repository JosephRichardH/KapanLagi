from django.db import models
from django.db.models import CharField
from django.shortcuts import render,redirect
from .models import Lagu
#from .forms import PostForm

# Create your views here.
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
