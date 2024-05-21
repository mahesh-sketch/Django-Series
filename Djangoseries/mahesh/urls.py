from django.urls import path
from . import views

urlpatterns = [
    path('',views.allComputerItem,name="item"),
]
