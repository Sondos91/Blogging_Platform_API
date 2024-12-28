from django.urls import path
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView,BlogDetailView,CategoryCreateView,SearchView,BlogFilterationView,BlogListView,TagDeleteView


urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:id>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', BlogDeleteView.as_view(), name='delete'),
    path('detail/<int:id>/', BlogDetailView.as_view(), name='detail'),
    #path('tag/create/', TagCreateView.as_view(), name='tag_create'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('search/', SearchView.as_view(), name='search'),
    path('filter/',BlogFilterationView.as_view(),name='filter'),
    path('list/',BlogListView.as_view(),name='list'),
    path('tag/delete/<int:id>/', TagDeleteView.as_view(), name='tag_delete'),
]