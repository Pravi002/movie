from django.urls import path
from API import views

urlpatterns=[
    path('movie/',views.MovieApi.as_view(),name="movie_api"),
    path('movies/<int:pk>/',views.Moviemixin.as_view(),name="movies"),


]