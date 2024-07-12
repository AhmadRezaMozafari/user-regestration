from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    shrot_intro = models.CharField(max_length=254)
    bio = models.TextField()
    avatar = models.ImageField(default='avatar.png',upload_to='images')

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)


    def __str__(self) -> str:
        return str(self.user.username)
    
