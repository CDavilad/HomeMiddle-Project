from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logoutaccount, name='logout'),
    path('login/', LogInView.as_view(), name='login'),
]