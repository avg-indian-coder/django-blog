from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

def createpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        created_at = str(datetime.now())
        data = Post(title=title,body=body,created_at=created_at)
        data.save()

        return redirect('index')
    return render(request, 'createpost.html')

def editpost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        created_at = str(datetime.now())
        post.title, post.body, post.created_at = title, body, created_at
        post.save()
        return redirect('index')
    
    return render(request, 'createpost.html', {'post': post})    

