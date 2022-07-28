from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Test2.serializers import PostSerializer
from .models import Post

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_post(request):
    serializer = PostSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Пост успешно создан")