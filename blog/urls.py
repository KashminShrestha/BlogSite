"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from blog import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", views.BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", views.BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="post_delete"),
]
