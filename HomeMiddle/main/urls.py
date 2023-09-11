from django.urls import path, include
from .views import *

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('authentication/', include('authentication.urls')),
    path('furnitures/', FurnitureIndexView.as_view(),name='furniture_index'),
    path('furnitures/<int:id>',FurnitureShowView.as_view(),name='show_furniture'),
    path('furnitures/<int:id>/reviews',ReviewsPage.as_view(),name='reviews'),
]