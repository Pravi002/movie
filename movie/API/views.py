from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from API.serializer import Movie_serializer
from film.models import movie

# Create your views here.

class MovieApi(APIView):
    def get(self,request,*args,**kwargs):
        qs=movie.objects.all()
        serializers=Movie_serializer(qs,many=True)
        return Response(data=serializers.data)
    def post(self,request,*args,**kwargs):
        serializers=Movie_serializer(data=request.POST)
        if serializers.is_valid():
            serializers.save()
            print("added")
            return Response(data=serializers.data)
        else:
            print("Not added")
        return Response(serializers.errors)



class Moviemixin(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=movie.objects.get(id=id)
        serializers=Movie_serializer(qs)
        return Response(data=serializers.data)

    
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=movie.objects.get(id=id)
        serializers=Movie_serializer(data=request.data,instance=qs)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie.objects.get(id=id).delete()
        return Response()
