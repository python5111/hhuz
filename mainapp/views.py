from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, CreateCourseForm
from .models import *

# Create your views here.

def main_page(request):
    jobs = Job_creat.objects.all()
    context={
        'jobs':'jobs',
    }
    return render(request, 'mainapp/baces.html',context)




def job_details(request):
    return render(request, 'mainapp/job_details.html')

def blog_page(request):
    return render (request, 'mainapp/blog.html')


def element_page(request):
    return render (request,'mainapp/elements.html' )

def single_blog(request):
    return render (request, 'mainapp/single-blog.html')

def job_list(request):
    return render (request, 'mainapp/job_listing.html')

def contact_page(request):
    return render (request, 'mainapp/single-blog.html')

def about_page(request):
    return render (request, 'mainapp/about.html')

def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
    context = {
        "form" : form
    }
    return render(request, 'mainapp/register.html',context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("main")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                messages.info(request,"Something was wrong")  

        context = {}

        return render(request,'mainapp/login.html', context)
    
 
@login_required(login_url='login')
def crest_ad(request):
    return render(request,'mainapp/creat_ad.html')