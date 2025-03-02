from rest_framework import serializers

from publication.models import Publication, Like


class PublicationSerializer(serializers.ModelSerializer):
    number_likes = serializers.IntegerField()
    has_user_liked = serializers.BooleanField()
    class Meta:
        model = Publication
        fields = '__all__'

class PublicationInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    body = serializers.CharField()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'