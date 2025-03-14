from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from blog.models import Post
from .serializers import PostSerializer
from django.db.models import Q



# Create your views here.

class PostAPIView(APIView):
    def get(self, request, *args, **kwargs):
        q_target = Q()
        
        if('id' in request.GET):
            id_get = request.GET.get('id')
            q_target &= Q(id = id_get)
        queryset = Post.objects.filter(q_target)
        serializer = PostSerializer(queryset, many = True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)