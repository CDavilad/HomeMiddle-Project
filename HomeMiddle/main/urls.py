from django.urls import path, include
from .views import *

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('authentication/', include('authentication.urls'))
]