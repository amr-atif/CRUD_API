from django.urls import path
from .views import PostsListApi,PostDetailApi

urlpatterns = [ 
    path('<int:pk>/',PostDetailApi.as_view(),name = 'post_detail'),
    path('',PostsListApi.as_view(),name='post_list'),
    
]