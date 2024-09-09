from django.db import models

# Create your models here.
from django.contrib.auth.models import User
choice=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
class Item(models.Model):
 name=models.CharField(max_length=255)
 description=models.TextField(blank=True,null=True)
 price=models.FloatField()
 image=models.ImageField( upload_to="static/profile/images",blank=True,null=True)
 rating=models.FloatField(default=0,choices=choice)
 quantity= models.IntegerField()
 created_by=models.ForeignKey(User,related_name="item",on_delete=models.CASCADE)
 created_at=models.DateTimeField( auto_now_add=True)
 def __str__(self):
  return self.name

class ReviewRating(models.Model):
  item=models.ForeignKey(Item,on_delete= models.CASCADE)
  created_by=models.ForeignKey(User,on_delete=models.CASCADE)
  subject = models.CharField(max_length=255,blank=True)
  review= models.TextField(max_length=500,blank=True)
  rating=models.IntegerField(default=0,choices=choice)
  ip=models.CharField(max_length=20,blank=True)
  status=models.BooleanField(default=True)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.subject

