from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login,logout
from .forms import *


# Create your views here.



@login_required(login_url='login')
def index(request):
    mess=None
    if request.method == "POST":
        blogs=blogForm(request.POST ,  request.FILES)
        if blogs.is_valid():
            blogs.save()
            mess="blog Post"
        else:
             mess="error"

    else:
       initial_data={'title':'','description':''}
       blogs=blogForm(initial=initial_data)
    context={
        'mess':mess,
        'blog':blogs
    }
    return render(request,"index.html",context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("login")  
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, "signup.html", context)

def user_login(request):  # Changed function name to avoid conflict
    mess = None
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  # Added request as the first argument
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) 
            return redirect('home')

        

    else:
        form = AuthenticationForm()
      
    context = {
        'form': form,
        'mess': mess
    }
    return render(request, "login.html", context)



def dashboard_view(request):
    blogs=blog.objects.all().distinct()
    pagination=Paginator(blogs,2)
    page_number=request.GET.get('page')
    blogs_part=pagination.get_page(page_number)
    return render(request,'dashboard.html',{'blogs':blogs_part})


def Edit_view(req,id):
    blogs=get_object_or_404(blog,id=id)
    return render(req,'editblog.html',{'blog':blogs})



def logout_view(req):
    logout(req)
    return redirect('login')




def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})
