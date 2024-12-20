from rest_framework import serializers
from .models import Blog, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'blog']  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name'] 
    
    def create(self, validated_data):
        category= Category.objects.create(**validated_data)
        return category

    def create(self, validated_data):
        tag= Tag.objects.create(**validated_data)
        return tag
class BlogSerializer(serializers.ModelSerializer):
    Tags = TagSerializer(many=True,required=False)
    Category = CategorySerializer(many=False,required=False)
    class Meta:
        model = Blog
        fields = ['Title', 'Content', 'Author','Tags']

    def create(self, validated_data):
        blog= Blog.objects.create(**validated_data)
        return blog


