from django.db import models
from userauth.models import User,Profile,user_directory_path

from shortuuid.django_fields import ShortUUIDField
import shortuuid
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.utils.html import format_html

TYPE=(
    ('food','food'),
    ('life style','life style'),
    ('travel','travel'),
)

    
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300,blank=True,null=True)
    image=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    text=models.TextField(null=True,blank=True)
    video=models.FileField(upload_to=user_directory_path,null=True,blank=True)
    category=models.CharField(max_length=100,choices=TYPE,default='travel')
    pid=ShortUUIDField(length=7,max_length=25,alphabet='abcdefghijklmnopqrstuvwxyz')
    likes=models.ManyToManyField(User,blank=True,related_name='likes')
    slug=models.SlugField(unique=True)
    views=models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.user.username
    
    def mark_as_featured(self):
        self.is_featured = True
        self.save()
        
    def save(self,*args,**kwargs):
        uuid_key=shortuuid.uuid()
        uniqueid=uuid_key[:4]
        if self.slug=='' or self.slug==None:
            self.slug=slugify(self.title) + '-' + uniqueid
        super(Post,self).save(*args,**kwargs)
        
    def post_comments(self):
        comments=Comment.objects.filter(post=self,active=True).order_by('-date')
        return comments
    
        
class Comment(models.Model):
    cid=ShortUUIDField(length=7,max_length=25,alphabet='abcdefghijklmnopqrstuvwxyz')
    user=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000) 
    active=models.BooleanField(default=True)
    likes=models.ManyToManyField(User,blank=True,related_name='comment_likes')
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.post)
    
    class Meta:
        verbose_name_plural='comment'
        
    def comment_replies(self):
        comment_reply=ReplyComment.objects.filter(comment=self,active=True)
        return comment_reply
        
class ReplyComment(models.Model):
    rid=ShortUUIDField(length=7,max_length=25,alphabet='abcdefghijklmnopqrstuvwxyz')
    user=models.ForeignKey(User,related_name='reply_user',on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    reply=models.CharField(max_length=1000) 
    active=models.BooleanField(default=True)
   
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.comment)
    
    class Meta:
        verbose_name_plural='Reply Comment'
    

