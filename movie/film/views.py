from django.shortcuts import render,redirect
from django.views.generic import View
from film.forms import GenreForm,MovieForm
from film.models import genre,movie
from django.contrib import messages
# Create your views here.

#Genre ADD
class GenreView(View):
    def get(self,request,*args,**kwargs):
        form=GenreForm()
        return render(request,"gen_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=GenreForm(request.POST)
        if form.is_valid():
            form.save()                                          
            messages.success(request,"genre add successfully")
            form=GenreForm()
        else:
            messages.error(request,"failed to add")
        return redirect("genre_list")    
        
#Movie ADD
class MovieView(View):
    def get(self,request,*args,**kwargs):
        form=MovieForm()
        return render(request,"mov_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"movie add successfully")
            form=MovieForm()
        else:
            messages.error(request,"failed to add")
        return redirect("movie_list")
        
#LIST 
        
#GENRE LIST
class GenreList(View):
    def get(self,request,*args,**kwargs):
        qs=genre.objects.all()
        print(request.GET)
        return render(request,"gen_list.html",{"qs":qs})
    
#MOVIE LIST
class MovieList(View):
    def get(self,request,*args,**kwargs):
        qs=movie.objects.all()
        print(request.GET)
        return render(request,"mov_list.html",{"qs":qs})
    
#GENRE DETAILS
class GenreDetails(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=genre.objects.get(id=id)
        return render(request,"gen_view.html",{"data":qs})
    
#MOVIE DETAILS
class MovieDetails(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=movie.objects.get(id=id)
        return render(request,"mov_view.html",{"data":qs})
    
#GENRE UPDATE
class GenreUpdate(View):
    def get(self,request,*args,**kwargs):
        data=kwargs.get("pk")
        obj=genre.objects.get(id=data)
        form=GenreForm(instance=obj)
        return render(request,"gen_update.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        data=kwargs.get("pk")
        obj=genre.objects.get(id=data)
        form=GenreForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        else:
            print("get out")
        return redirect("genre_list")
    
# Movie Update
class MovieUpdate(View):
    def get(self,request,*args,**kwargs):
        data=kwargs.get("pk")
        obj=movie.objects.get(id=data)
        form=MovieForm(instance=obj)
        return render(request,"mov_update.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        data=kwargs.get("pk")
        obj=movie.objects.get(id=data)
        form=MovieForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        else:
            print("get out")
        return redirect("movie_list")
    
#GNERE DELETE
class GenreDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        genre.objects.get(id=id).delete()
        return redirect('genre_list')
    
#Movie Delete
class MovieDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie.objects.get(id=id).delete()
        return redirect('movie_list')