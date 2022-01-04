from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="Blog-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="Blog-about"),
    path("search_post/", views.search_post, name="search-post"),
    path("Periodic_Table/", views.Periodic_Table, name="periodic-table"),
    path("user_manual/", views.user_manual, name="user-manual"),
    path('download/<str:path>', views.download, name='download'),    
]

