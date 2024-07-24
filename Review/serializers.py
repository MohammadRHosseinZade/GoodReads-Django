from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'rating']  
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('user', None)  
        validated_data.pop('book', None)
        return super().update(instance, validated_data)