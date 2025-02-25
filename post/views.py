from rest_framework import generics
from .models import Category, Comment, Tag, Post
from .serializers import CategorySerializer, TagSerializer, PostSerializer, CommentSerializer
from rest_framework.views import APIView, Http404
from rest_framework.response import Response
from rest_framework import status


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        if category_id:
            return Category.objects.filter(id=category_id)
        return Category.objects.all()


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        tag_id = self.kwargs.get('pk')
        if tag_id:
            return Tag.objects.filter(id=tag_id)
        return Tag.objects.all()


# POST
class PostListCreateView(generics.ListCreateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

class PostDetailAPIView(APIView):
    def get_post(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# COMMENT
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentAPIView(APIView):
    def get(self, request, pk):
        try:
            comments = Comment.objects.filter(Comment_id=pk)
        except Comment.DoesNotExist:
            raise Http404

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        data = request.data.copy()
        data['post'] = pk
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)