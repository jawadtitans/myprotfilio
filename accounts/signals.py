from django.db.models.signals import pre_save,post_save
from .models import userprofile,User
from django.dispatch import receiver
@receiver(post_save,sender=User)
def post_save_create_profile_user(sender,instance,created,**kwargs):
    if created:
        userprofile.objects.create(user=instance)
        print("the user profile created")
    else:
        try:
            userprofile.objects.get(user=instance)
            userprofile.save()
        except:
            userprofile.objects.create(user=instance)
            print(" user profile uploaded")

# #  of course there is no need to write this line of code for awarning of creating the useprofile but we show how we can do this in here.
# @receiver(pre_save,sender= User,)
# def pre_save_userprofile(instance,sender,**kwargs):
#     print(instance.username,"this user being created ")


     
    
