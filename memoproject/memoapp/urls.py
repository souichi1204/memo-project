from django.contrib import admin
from django.urls import path,include
from .views import Memolist,Memodetail,Memodelete,Memoupdate

urlpatterns = [
    path('list/',Memolist.as_view(),name='list'),
    path('detail/<int:pk>',Memodetail.as_view(),name='detail'),
    path('delete/<int:pk>',Memodelete.as_view(),name='delete'),
    path('update/<int:pk>',Memoupdate.as_view(),name='update'),
]
