from rest_framework import serializers 
from main.models import Furniture 

 

class HomeMiddleSerializer(serializers.ModelSerializer): 

    class Meta: 

        model = Furniture 
        fields = ['id', 'name', 'type', 'maker', 'material', 'description', 'price', 'associated_furnitures', 'image_url']