from django.db import models
from uuid import uuid4
from django.utils.text import slugify

# Create your models here.
#models are represented by a class

    #add in thumbnail 
    #author

    #python manage.py makemigrations
    #python manage.py migrate 
class Article(models.Model):
     title = models.CharField(max_length= 100)
     slug = models.SlugField()
     body = models.TextField()
     date = models.DateTimeField(auto_now_add= True)
     
     

     def __str__(self):
         return self.title
     

     def snippet(self):
          return self.body[:50] + "...."
     

     
class GCs(models.Model):
     GC_ID = models.IntegerField(primary_key= True)
     GC_Name = models.CharField(max_length= 100)
     GC_Type = models.CharField(max_length= 10)
     GC_Photo = models.ImageField(upload_to = 'assets/' , null= True)
     GC_Desc = models.TextField(max_length= 200)

     def __str__(self):
         return self.GC_Name

class Score_Board(models.Model):
     GC_ID = models.IntegerField(primary_key= True)
     Points_Array = models.JSONField()

     def __int__(self):
         return self.GC_ID
     

class Hostel(models.Model):
    """Entry for each hostel."""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40, blank=True)
    short_name = models.CharField(max_length=25, blank=True)
    long_name = models.CharField(max_length=100, blank=True)
    Cult_Points = models.IntegerField( default= 0)
    Tech_Points = models.IntegerField( default= 0)
    Sports_Points = models.IntegerField( default= 0)
    Total_Points = models.IntegerField( default=0)
    #mess_gsheet = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)