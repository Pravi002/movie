from django.db import models

# Create your models here.

#Genre
class genre(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
#Movie
class movie(models.Model):
    title=models.CharField(max_length=100)
    release_date=models.CharField(max_length=20)
    duration=models.CharField(max_length=20)
    summary=models.TextField(max_length=500)
    genre=models.ForeignKey(genre,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
