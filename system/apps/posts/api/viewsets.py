from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Model
from apps.posts.models import Post
# Serializers
from . import serializers
# Permissions
from .permissions import IsAdminOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ ModelViewSet para el modelo Post """
    permission_classes = [IsAdminOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # http_method_names = ['get']


# class PostViewSet(viewsets.ViewSet):
    
#     def list(self, request, *args, **kwargs):
#         queryset = Post.objects.all()
#         serializer = serializers.PostSerializer(queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def create(self, request, *args, **kwargs):
#         serializer = serializers.PostSerializer(data=request.data)
#         if serializer.is_valid():
#             instance = serializer.save()
#             serializer = serializers.PostSerializer(instance)
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk: int, *args, **kwargs):
#         queryset = Post.objects.get(pk=pk)
#         serializer = serializers.PostSerializer(queryset)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    