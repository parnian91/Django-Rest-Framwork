from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
def index_page(request):
    context  = {
        'posts': Post.objects.all(),
    }
    return render(request,'posts/index.html',context)