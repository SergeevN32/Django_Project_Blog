from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from random import sample
from django.db.models import F
from .models import Post
from .models import AboutMe
from django.views.generic import ListView


# Create your views here.


def index(request):
    author_content = AboutMe.objects.all()[0]
    posts_content = Post.objects.order_by('?')[:3]
    return render(request, 'blog/index.html', context={
        'posts_content': posts_content,
        'author_content': author_content,
    })



# class ListPostsView(ListView):
#     model = Post
#     template_name = 'blog/list_detail.html'
#     context_object_name = 'posts_content'

def posts(request):
    author_content = AboutMe.objects.all()[0]
    posts_content = Post.objects.all().order_by('-date')
    return render(request, 'blog/list_detail.html', context={
        'posts_content': posts_content,
        'author_content': author_content,
                                                             })


def get_info_about_post(request, slug_post: str):
    author_content = AboutMe.objects.all()[0]
    post = get_object_or_404(Post, slug=slug_post)
    return render(request, 'blog/detail_by_name.html', context={
        "post": post,
        'author_content': author_content,
    })


def get_info_about_author(request):
    author_content = AboutMe.objects.all()[0]
    return render(request, 'blog/info_author.html', context={'author_content': author_content, })
