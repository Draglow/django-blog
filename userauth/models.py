from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from PIL import Image
from shortuuid.django_fields import ShortUUIDField
import shortuuid
from django.utils.text import slugify
from django.db.models.signals import post_save


def user_directory_path(instance,filename):
    ext=filename.split('.')[-1]
    filename="%s.%s" % (instance.user.id,ext)
    return 'user_{0}/{1}'.format(instance.user.id,filename)



from django.contrib.auth.models import AbstractUser, Permission

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Add the groups field with a unique related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='user_custom_groups'  # Change related_name to avoid clash
    )

    # Add the user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='user_custom_permissions'  # Change related_name to avoid clash
    )

    def __str__(self):
        return self.username

        
    
class Profile(models.Model):
    pid=ShortUUIDField(length=7,max_length=25,alphabet='abcdefghijklmnopqrstuvwxyz')
    image=models.ImageField(upload_to=user_directory_path,null=True,blank=True,default='default.jpg')
    cover_image=models.ImageField(upload_to=user_directory_path,null=True,blank=True,default='cover.jpg')
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    full_name=models.CharField(max_length=100,null=True,blank=True)
    slug=models.SlugField(unique=True,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
            
    def save(self,*args,**kwargs):
        if self.slug=='' or self.slug==None:
            uuid_key=shortuuid.uuid()
            uniqueid=uuid_key[:2]
            self.slug=slugify(self.full_name) + '-' + str(uniqueid.lower())
        super(Profile,self).save(*args,**kwargs)
            
    #class Meta:
        #prepopulated_fields = {'slug': ('full_name',)}
        
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()