"""Afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from movie_app import views
from . import yasg
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/directors', views.director_view),
    # path('api/v1/directors/<int:id>/', views.director_detail_view),
    path('api/v1/movies/', views.MovieListCreateAPIView.as_view()),
    path('api/v1/movies/<int:id>', views.movie_detail_view),
    # path('api/v1/reviews/', views.review_view),
    # path('api/v1/reviews/<int:id>/', views.review_detail_view),
    path('api/v1/profiles/', include('profiles.urls')),
    path('api/v1/directors', views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewModelViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/reviews/<int:id>/', views.ReviewModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
]

urlpatterns += yasg.urlpatterns
