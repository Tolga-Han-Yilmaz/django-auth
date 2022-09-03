from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
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
            # Bundan sonraki işlemler extra
            username = form.cleaned_data.get("username") 
            password = form.cleaned_data.get("password")
            return redirect("login")
    context={
        "form":form
    }
    return render(request,"registration/register.html",context)