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


def test1(request):
    return render(request,'mainapp/temp.html')

def job_details(request,pk):
    job_detail = Job_creat.objects.get(id = pk)
    
    context = {
        "job_detail" : job_detail 
    }
    
    return render(request, 'mainapp/job_details.html',context)

def blog_page(request):
    blogs = Blog.objects.all().order_by("-id")
    context = {
        "blogs" : blogs
    }
    return render (request, 'mainapp/blog.html',context)


def element_page(request):
    return render (request,'mainapp/elements.html' )

def single_blog(request):
    return render (request, 'mainapp/single-blog.html')

def job_list(request):
    job_lists = Job_creat.objects.all().order_by("-id")
    
    context = {
        "job_lists" : job_lists 
    }
    return render (request, 'mainapp/job_listing.html',context)

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