from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer, TagSerializer, CategorySerializer
from .models import Blog , Tag , Category
from rest_framework.permissions import IsAdminUser, BasePermission
from django.db.models import Q
from .pagination import BlogPagination
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound

# Create your views here.

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.Author == request.user


class BlogCreateView(APIView):
    def post(self, request,*args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BlogDetailView(APIView):
    def get(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=200)

class BlogUpdateView(APIView):
    permission_classes = [IsOwner]

    def get_object(self,id):
        try:
            obj = Blog.objects.get(id=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except Blog.DoesNotExist:
            raise NotFound ('Blog not found')

    def put(self, request, *args, **kwargs):
        blog = self.get_object(kwargs['id'])
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class BlogDeleteView(APIView):
    permission_classes = [IsOwner|IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_object(self,id):
        try:
            obj = Blog.objects.get(id=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except Blog.DoesNotExist:
            raise NotFound ('Blog not found')

    def delete(self, request, *args, **kwargs):
        blog = self.get_object(kwargs['id'])
        blog.delete()
        return Response(status=204)

# class TagCreateView(APIView):
#     def post(self, request,*args, **kwargs):
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
class TagDeleteView(APIView):
    def delete (self, request, *args, **kwargs):
        tag = Tag.objects.get(id=kwargs['id'])
        tag.delete()
        return Response(status=204)
    
class CategoryCreateView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request,*args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        blogs = Blog.objects.filter(Q(Title__icontains=query) | Q(Content__icontains=query)| Q(Tags__name__icontains=query)| Q (Author__username__icontains=query))
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)

class BlogFilterationView(APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('Category', '')
        author = request.query_params.get('Author', '')
        tag = request.query_params.get('Tag', '')
        blogs = Blog.objects.filter(Q(Category__name=category)|Q(Author__username=author)|Q(Tags__name=tag))
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)

class BlogListView(APIView):
    pagination_class = BlogPagination
    filter_backends = [OrderingFilter]
    ordering_fields = [ 'Category', 'Published_Date']
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(Published_Date__isnull=False).all()
        paginator = self.pagination_class()
        sort_by= request.query_params.get('sort_by', '')
        if sort_by:
            blogs = blogs.order_by(sort_by)
        page = paginator.paginate_queryset(blogs, request, view=self)
        if page is not None:
            serializer = BlogSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)
