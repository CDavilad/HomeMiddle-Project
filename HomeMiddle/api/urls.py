from django.urls import path 
from . import views 

urlpatterns = [ 
    path('furniture/', views.FurnitureList.as_view(), name="list"), 
] 