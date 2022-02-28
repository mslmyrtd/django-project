
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def home(request):
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={
        "form":form
    }
    return render(request,"home/index.html",context)
def teacher(request):
    return render(request,"home/teacher.html")
def about(request):
    return render(request,"home/about.html")

