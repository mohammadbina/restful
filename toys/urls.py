from django.urls import path, re_path
from . import views

urlpatterns = [
        re_path(r'^toys/$', views.toy_list, name='toy_list'),
        re_path(r'^toys/(?P<pk>[0-9]+)/$', views.toy_detail, name='toy_detail'),
        
        
        
        
        
        
        ]
