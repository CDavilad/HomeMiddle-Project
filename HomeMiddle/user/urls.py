from django.urls import path
from .views import *

urlpatterns = [
    path('settings/',UserConfig.as_view(),name='settings'),

]