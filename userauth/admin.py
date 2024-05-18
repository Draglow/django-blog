from django.contrib import admin
from userauth.models import User
from userauth.models import Profile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['username','full_name','username','email']
    list_display_links=['full_name','username']
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','full_name',]
    list_display_links=['full_name','user']
    

admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)