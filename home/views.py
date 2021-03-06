
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Teacher
# Create your views here.
import random
def home(request):
    items=list(Teacher.objects.all())
    teachers=random.sample(items,2)
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={
        "form":form,
        "teachers":teachers
    }
    return render(request,"home/index.html",context)
def teacher(request):
    teachers= Teacher.objects.all()
    context={
        "teachers":teachers
    }
    return render(request,"home/teacher.html",context)
def about(request):
    return render(request,"home/about.html")

