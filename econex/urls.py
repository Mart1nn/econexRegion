from django.urls import path

from .views import *


urlpatterns = [
    path('',                 posts_list,   name='posts_list_url'),
    path('post/<str:slug>/', post_detail,  name='post_detail_url'),
    path('seria/<int:pk>/',  seria_detail, name='seria_detail_url'),
    path('contact/',         contact,      name='contact_url')
]