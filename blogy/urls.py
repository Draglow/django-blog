
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from userauth import views


urlpatterns = [
    path('admin/logout/', views.logout_view, name='admin_logout'),
    path("admin/", admin.site.urls),
    path("", include('blog.urls')),
    path("", include('userauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
