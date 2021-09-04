from rest_framework import serializers

from apps.core.models import AnimeProfile, Anime, Source
from apps.manganelo_api.services import add_anime_to_user


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        exclude = ('anime',)


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'


class AnimeAddViewSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    authors = serializers.CharField(max_length=256)
    chapter_count = serializers.FloatField()
    views = serializers.IntegerField()
    image = serializers.URLField()
    ratings = serializers.FloatField()
    last_updated = serializers.DateField()
    url = serializers.URLField()
    type = serializers.CharField(max_length=256)

    def validate(self, attrs):
        source_serializer = SourceSerializer(data=attrs)
        source_serializer.is_valid(raise_exception=True)

        anime_serializer = AnimeSerializer(data=attrs)
        anime_serializer.is_valid(raise_exception=True)

        add_anime_to_user(
            anime_data=anime_serializer.validated_data,
            source_data=source_serializer.data,
            user=self.context.get('request').user
        )
        return attrs
