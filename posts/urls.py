from .views import PostList, PostDetail, index_page
from django.urls import path

urlpatterns = [
    path('', index_page),
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),

]



