from rest_framework import serializers
from blog.models import Blogs, Tags, Category
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields='__all__'
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value
    def validate_content(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Content is too short.")
        return value

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'