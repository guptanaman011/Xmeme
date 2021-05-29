from rest_framework import serializers
from .models import imagedata

class imagedataserializers(serializers.ModelSerializer):
    class Meta:
        model=imagedata
        fields = ('id',
         'name',
         'caption',
         'url')

