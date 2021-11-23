from django.contrib import admin
from django.urls import path,re_path
from. import views


urlpatterns = [
 
    path('',views.index,name='index'),
    path('home',views.index,name='home'),
    path('upload',views.upload,name='upload'),
    path('cluster',views.cluster,name='cluster'),
    path('calculate',views.calculate,name='calculate'),
    path('compute2d',views.compute2d,name='compute2d'),
    path('compute3d',views.compute3d,name='compute3d'),
    path('compareCIFs',views.compareCIFs,name='compareCIFs'),
    path('computeDistMatrix',views.computeDistMatrix,name='computeDistMatrix'),
    path('upload_file',views.upload_file,name='upload_file'),
    path('remove_file',views.remove_file,name='remove_file'),
    path('getMediaFiles',views.getMediaFiles,name='getMediaFiles'),

]
