from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_daate = timezone.now()
            post.save()
            if request.POST.get('_save'):
                return redirect('post_details', pk=post.pk)
            if request.POST.get('_addanother'):
                return redirect('post_new')
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {'form':form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        '''
        print('*' * 10)
        print(request.POST)
        print(request.POST.get('_save', '_save_none'))
        print(request.POST.get('_addanother', '_addanother_none'))
        print(request.method)
        print(dir(request))
        print(type(request.user))
        print(request.user)
        print('*' * 10)
        '''
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            if request.POST.get('_save'):
                return redirect('post_details', pk=post.pk)
            if request.POST.get('_addanother'):
                form = PostForm()
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})
