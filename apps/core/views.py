from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.serializers import AnimeAddViewSerializer


class AddAnime(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, ]

    def post(self, request):
        serializer = AnimeAddViewSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response()


class GetAnime(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, ]

    def get(self, request):
        a = []
        for k, i in enumerate(request.user.tracker.animes):
            anime_data = i.anime.sources.first()
            a.append(
                {
                    'id': k,
                    'anime_profile': {
                        'current_chapter': i.current_chapter,
                        'last_time_read': i.last_time_read,
                    },

                    'anime_data': {
                        'title': anime_data.title,
                        'authors': anime_data.authors,
                        'last_updated': anime_data.last_updated,
                        'chapter_count': anime_data.chapter_count,
                        'views': anime_data.views,
                        'image': anime_data.image
                    }
                }
            )

        return Response(a)
