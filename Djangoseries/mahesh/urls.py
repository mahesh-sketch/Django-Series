from django.urls import path
from . import views

urlpatterns = [
    path('',views.allComputerItem,name="item"),
    path('<int:comp_id>/',views.computer_detail,name="comp_detail"),
    path('comp_store/',views.computer_store_view,name="comp_store")
]
