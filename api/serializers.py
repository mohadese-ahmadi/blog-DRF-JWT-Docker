from rest_framework import serializers
from blog.models import Blogs, Tags, Category
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields='__all__'
    def validate_title(self, value):
        if len(value)<5:
            raise serializers.ValidationError("Title must be more than 5 chars")
        return value
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'