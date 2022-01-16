from rest_framework import serializers
# Models
from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            # "id": instance.id,
            "titulo": instance.title,
            "descripcion": instance.description,
            "orden": instance.order,
            "created_at": instance.created_at,
        }
    
    def validate_order(self, data):
        if data < 0:
            raise serializers.ValidationError("Solo valores positivos")
        return data
    
    def validate_empty_values(self, data):
        return super().validate_empty_values(data)