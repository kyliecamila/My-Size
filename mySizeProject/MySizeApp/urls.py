from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name = "home"),
    path('top', views.topView, name = "topView"),
    path('top', views.topView, name = "topView"),
    path('compare/<int:id>', views.compareView, name = "compareView" )
   
]