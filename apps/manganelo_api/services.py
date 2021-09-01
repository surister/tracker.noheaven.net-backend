from apps.core.models import Anime


def get_or_create_anime(attrs: dict) -> Anime:
    queryset = Anime.objects.filter(title__icontains=attrs.get('title'))

    if queryset.exists():
        return queryset.first()

    attrs.pop('id')

    return Anime.objects.create(
        **attrs
    )
