from django.shortcuts import render, get_object_or_404
from .forms import AddPostForm
from .models import Post
from django.shortcuts import redirect
from actions.utils import create_action
from actions.models import Action


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                create_action(request.user, 'добавив пост')
                post.save()
                # return redirect('add_post', pk=post.pk)
                return redirect('dashboard')
    else:
        form = AddPostForm()
    return render(request, 'content/post/post_create.html', {'form': form})


def post_list(request):
    template = 'content/post/post_list.html'
    posts = Post.objects.filter(status='published')
    context = {'posts': posts, 'section': 'posts'}
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'content/post/post_detail.html'
    context = {'post': post}
    return render(request, template, context)


# def add_post(request):
#     form = AddPostForm()
#     return render(request, 'content/post/post_create.html', {'form': form})
