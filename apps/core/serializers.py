from django.contrib.auth.models import User

from rest_framework import serializers

from apps.manganelo_api.services import get_or_create_anime


class AnimeAddSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=256)
    source = serializers.CharField(max_length=256)

    def validate(self, attrs):
        anime = get_or_create_anime(attrs)
        user = User.objects.get(id=3)
        user.tracker.anime_set.add(anime)
        return attrs
