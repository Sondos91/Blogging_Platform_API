from django.urls import path
from .views import UserRegisterView, UserLoginView, UserView, UpdateProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user/', UserView.as_view() , name='user'),
    path('update/<int:user_id>/', UpdateProfileView.as_view(), name='update'),
]