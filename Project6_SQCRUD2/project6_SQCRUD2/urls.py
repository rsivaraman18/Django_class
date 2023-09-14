from django.contrib import admin
from django.urls import path
from Upload_app import views   
       
''' Medis path kuduka itha import pandran'''
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.Lets_Register),
    path('',views.Lets_View,name="dis_view"),
    path('update/<int:cid>',views.Lets_update),
    path('delete/<int:cid>',views.Lets_delete),
     
]




# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
