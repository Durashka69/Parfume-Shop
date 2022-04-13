from rest_framework import serializers
from main.models import *


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ('value',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('title',)


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('title',)


class TypeOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_of
        fields = ('title',)


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('title',)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title',)


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('user', 'comment', 'content', 'created', 'updated')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        ref_name = 'UserTest'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'product', 'content',
                  'created', 'updated', 'replies')


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('user', 'score', 'product')


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    volume = VolumeSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    purpose = PurposeSerializer(read_only=True)
    type_of = TypeOfSerializer(read_only=True)
    family = FamilySerializer(read_only=True)
    note = NoteSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'year', 'image', 'brand', 'volume',
                  'purpose', 'type_of', 'price', 'code', 'family', 
                  'note', 'description', 'for_men', 'available', 'comments', 'ratings')
