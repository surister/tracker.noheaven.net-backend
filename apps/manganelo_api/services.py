import datetime

from django.contrib.auth.models import User

from apps.core.models import Anime, AnimeProfile, Source


def add_anime_to_user(anime_data: dict, source_data, user: User):
    """
    Creates Anime if it does not exist.
    Crates AnimeProfile.

    :param anime_data:
    :param anime_profile_data:
    :param attrs:
    :param user:
    :return:
    """

    queryset = Anime.objects.filter(title__icontains=anime_data.get('title'))

    if queryset.exists():
        anime_obj = queryset.first()
    else:
        anime_obj = Anime.objects.create(
            **anime_data
        )

    anime_profile_obj = AnimeProfile.objects.create(tracker=user.tracker, anime=anime_obj)

    Source.objects.create(anime=anime_obj, **source_data)
