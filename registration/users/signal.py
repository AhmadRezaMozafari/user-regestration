from .models import User,Profile
from django.db.models.signals import post_save,post_delete


def createProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            email = user.email,
            name = user.first_name
        )


post_save.connect(createProfile,sender=User)