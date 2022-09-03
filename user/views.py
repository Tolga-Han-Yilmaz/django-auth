from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,"user/home.html")

def register(request):
    form = UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # buraya kadar ki işlemler kullanıcının register olması için yeterli. 
            # register ile birlikte login olmasını istiyorsak
            username = form.cleaned_data.get("username") 
            password = form.cleaned_data.get("password1")
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect("home")
    context={
        "form":form
    }
    return render(request,"registration/register.html",context)

@login_required  # sadece kayıtlı olan kişilerin görmesi için
def special(request):
    return render(request,"user/special.html")