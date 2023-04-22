from rest_framework import serializers
from .models import Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ReviewSerializerPUT(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['title','description', 'img']

