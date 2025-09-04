from rest_framework import serializers
from blog.models import Blogs, Tags, Category, Comment
from account.models import Author


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = [
            'id',
            'title',
            'description',
            'context',
            'category',
            'tag',
            'image_file']

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
        model = Tags
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'username', 'email', 'password', 'sex']
        extra_kwargs = {
            'password': {'write_only': True}}

    def create(self, validated_data):
        user = Author(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            sex=validated_data.get('sex', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post', 'content', 'parent', 'created_at', 'user']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'sex', 'is_superuser']
        read_only_fields = ['id', 'is_superuser']