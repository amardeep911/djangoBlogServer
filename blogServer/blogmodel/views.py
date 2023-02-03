from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from blogmodel.serializer import PostSerializer
from blogmodel.models import Post
# Create your views here.
class getAllBlogViews(APIView):
    def get(self, request, format=None):
        blogData = Post.objects.all()
        blogArray = []
        for a in blogData:
            blogArray.append({"blogTitle": a.blogTitle, "blogContent": a.blogContent,"blogId":a.id})
        # how to extract that specific unique key from my blog model so that i can send it with response
        return Response( {"data" : blogArray} ,content_type="application/json", status=status.HTTP_201_CREATED)


class PostListAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        data = {
            'blogContent': request.data.get('blogContent'),
            'blogTitle': request.data.get('blogTitle'),
        }
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'blog created'}, status = status.HTTP_201_CREATED,)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)