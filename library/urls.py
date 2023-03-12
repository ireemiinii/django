from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='library-home'),
    path('upload/', views.upload, name = 'library-upload'),
    path('upload/aca', views.upload_lnotes, name = 'library-upload_lnotes'),
    path('upload/stu', views.upload_snotes, name = 'library-upload_snotes'),
    path('snotes',views.snotes_list,name = 'library-snotes_list'),
    path('lnotes', views.lnotes_list,name= 'library-lnotes_list'),




] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

