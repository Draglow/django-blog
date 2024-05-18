from django.contrib import admin
from blog.models import Post,Comment,ReplyComment
from django.utils.html import format_html
# Register your models here.


class Admincomment(admin.ModelAdmin):
    
    
    list_display=['user','post','comment']
    list_display_links=['user','post']


class Adminreply(admin.ModelAdmin):
    
    
    list_display=['user','comment']
    list_display_links=['user','comment']

class PostGallery(admin.ModelAdmin):
    #inlines=[GalleryAdminTap]
    def thumbnail(self,object):
        return format_html("<img src='{}' width='40' style='border-radius:50px;' />".format(object.image.url))
    thumbnail.short_discription='image'

    list_display=['thumbnail','user','title']
    prepopulated_fields={'slug':('title',)}
    


admin.site.register(Post,PostGallery)

admin.site.register(Comment,Admincomment)

admin.site.register(ReplyComment,Adminreply)
