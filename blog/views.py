from django.shortcuts import render,redirect,get_object_or_404

import shortuuid
from . models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.

def index(request):
    posts=Post.objects.all()
    featured_post=Post.objects.filter(is_featured=True).order_by('-date')
    context={
        'posts':posts,
        'featured':featured_post
    }
    return render(request,'blog/index.html',context)


def post_detail(request,id):
    posts = get_object_or_404(Post, pk=id)
    
    
    context={
        'posts':posts
    }
    return render(request,'base/detail.html',context)
#@login_required
from django.shortcuts import render
from django.utils.text import slugify
import shortuuid
from .models import Post

def post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        text = request.POST.get('text')
        #category = request.POST.get('category')
        
        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:4]
        
        if title and image and text:
            post = Post(
                title=title,
                image=image,
                text=text,
                #category=category,
                user=request.user,
                slug=slugify(title) + '-' + str(uniqueid.lower()),
            )
            post.save()
            
            return redirect('index')  # Render success page after saving
        else:
            messages.error(request,'Invalid Credentials')
            print("Form data is incomplete or invalid:", request.POST.dict())
            # You can add more detailed error handling or logging here
    return render(request, 'blog/forms.html')
