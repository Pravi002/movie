"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from film.views import GenreView,GenreList,GenreDetails,GenreUpdate,GenreDelete
from film.views import MovieView,MovieList,MovieDetails,MovieUpdate,MovieDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("API.urls")),
    path('genreadd/',GenreView.as_view(),name='genre'),
    path('movieadd/',MovieView.as_view(),name='movie'),
    path('genrelist/',GenreList.as_view(),name="genre_list"),
    path('',MovieList.as_view(),name="movie_list"),
    path('genredetails/<int:pk>',GenreDetails.as_view(),name='gen-details'),
    path('moviedetails/<int:pk>',MovieDetails.as_view(),name='mov-details'),
    path('genreupdate/<int:pk>/update',GenreUpdate.as_view(),name="gen-update"),
    path('movieupdate/<int:pk>/update',MovieUpdate.as_view(),name="mov-update"),
    path('genredelete/<int:pk>/delete',GenreDelete.as_view(),name='gen-delete'),
    path("moviedelete/<int:pk>/delete",MovieDelete.as_view(),name="mov-delete")
]
