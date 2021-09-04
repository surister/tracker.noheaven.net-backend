from django.http import HttpResponse
from rest_framework.views import APIView

from apps.authentication.serializers import LoginSerializer


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return HttpResponse()
