from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend

from main.filters import ProductFilter
from main.models import Product, Comment, Reply, Rating
from main.serializers import ProductSerializer, CommentSerializer, RatingSerializer, ReplySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissoon_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
