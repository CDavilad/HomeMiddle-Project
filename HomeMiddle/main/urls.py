from django.urls import path, include
from .views import *

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('authentication/', include('authentication.urls')),
    path('user/', include('user.urls')),
    path('shoppingcart/', show_shopping_cart,name='shopping_cart'),
    path('shoppingcart/buy', buy, name='buy'),
    path('added_to_sc/', AddedToShoppingCart.as_view(),name='added_to_sc'),
    path('shoppingcart/remove_from_sc/<int:furniture_id>/', remove_from_shopping_cart, name='remove_from_sc'),
    path('furnitures/', FurnitureIndexView.as_view(),name='furniture_index'),
    path('furnitures/add_to_sc/<int:furniture_id>/', add_to_shopping_cart, name='add_to_sc'),
    path('furnitures/add_to_wl/<int:furniture_id>/', add_to_wish_list, name='add_to_wl'),
    path('furnitures/<int:id>',FurnitureShowView.as_view(),name='show_furniture'),
    path('furnitures/<int:id>/reviews',ReviewsPage.as_view(),name='reviews'),
    path('wishlist/', show_wish_list,name='wish_list'),
    path('added_to_wl/', AddedToWishList.as_view(),name='added_to_wl'),
    path('wishlist/remove_from_wl/<int:furniture_id>/', remove_from_wish_list, name='remove_from_wl'),
]