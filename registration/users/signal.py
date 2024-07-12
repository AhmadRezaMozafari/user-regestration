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


def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email

def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteProfile, sender=Profile)

