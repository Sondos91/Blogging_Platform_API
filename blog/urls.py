from django.urls import path
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView,BlogDetailView


urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:id>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', BlogDeleteView.as_view(), name='delete'),
    path('detail/<int:id>/', BlogDetailView.as_view(), name='detail'),
]