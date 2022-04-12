from django.urls import path, include
from rest_framework import routers

from main.views import ProductListView, CommentViewSet, ReplyViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductListView, basename='products')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'replies', ReplyViewSet, basename='replies')
router.register(r'ratings', RatingViewSet, basename='ratings')

urlpatterns = [
    path('main/', include(router.urls))
]
