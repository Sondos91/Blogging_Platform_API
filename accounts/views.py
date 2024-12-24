from rest_framework.views import APIView
from .serializers import UserRegisterSerializer , UserLoginSerializer, UserSerializer   
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth import logout

# Create your views here.


class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class UserView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = User.objects.exclude(is_staff=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound
    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args , **kwargs):
        logout(request)
        return Response(status=204)

