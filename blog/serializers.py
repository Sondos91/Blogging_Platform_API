from rest_framework import serializers
from .models import Blog, Tag, Category
from accounts.models import User
from accounts.serializers import UserSerializer


class TagSerializer(serializers.ListField):
    class Meta:
        model = Tag
        fields = ['name']  
    def create(self, validated_data):
        
        tag= Tag.objects.create(**validated_data)
        return tag

    def to_representation(self, data):
        return data.values_list('name', flat=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name'] 
    
    def create(self, validated_data):
        category= Category.objects.create(**validated_data)
        return category

class BlogSerializer(serializers.ModelSerializer):
    Tags = TagSerializer(required=False)

    class Meta:
        model = Blog
        fields = ['Title', 'Content', 'Author','Tags', 'Category']

    def create(self, validated_data):
        tag_names = validated_data.pop('Tags', [])
        blog = Blog.objects.create(**validated_data)
        if tag_names:
            Tags = []
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                Tags.append(tag)
            blog.Tags.set(Tags)
        return blog
    
    def update(self,instance, validated_data):
        tag_names = validated_data.pop('Tags', []) 

        blog = super().update(instance, validated_data)
        
        if tag_names:
            Tags = []
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name)
                Tags.append(tag)
                
            blog.Tags.set(Tags)

        return blog
    
    def to_representation(self, instance):
        # Override to_representation to display tag names instead of IDs
        representation = super().to_representation(instance)
        representation['Category'] = CategorySerializer(instance.Category).data if instance.Category else None
        representation['Author'] = UserSerializer(instance.Author).data.get ('username') 
        return representation


