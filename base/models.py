from django.db import models

# Create your models here.
class Students(models.Model):
   name = models.CharField(max_length=50,null=True,blank=True)
   age = models.IntegerField()
   image = models.ImageField(upload_to='Posted_Images', blank=True, null=True,)
   # image = models.ImageField(upload_to='students/Posted_Images', blank=True, null=True)
   # image = models.ImageField(upload_to='Posted_Images', blank=True, null=True, default=None)
   
   def __str__(self):
          return self.name