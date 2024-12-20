from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['Title', 'Content', 'Author']

    def create(self, validated_data):
        blog= Blog.objects.create(**validated_data)
        return blog