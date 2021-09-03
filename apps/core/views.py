from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.serializers import AnimeAddSerializer


class AddAnime(APIView):
    def post(self, request):
        serializer = AnimeAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response()
