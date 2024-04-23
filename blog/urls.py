from django.urls import path
from . import views as views_blog

urlpatterns = [
    path('', views_blog.index, name='index'),
    path('posts/', views_blog.posts, name='all-posts'),
    # path('posts/', views_blog.ListPostsView.as_view(), name='all-posts'),
    path('posts/<slug:slug_post>', views_blog.get_info_about_post, name='post-name'),
    path('author/', views_blog.get_info_about_author, name='info-author'),
]