from django.db import models
from django.contrib.auth.models import User # this data from admin panel 


# Create your models here.



class Tweet(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)# this is for user connected and save from massv delete
    text = models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photos/', blank=True,null=True)# image upload and also null allowd 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)# when add data that time update 
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'  #when clcl urle we can modified this
    
