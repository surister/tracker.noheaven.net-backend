from django.http import HttpResponse
from rest_framework.views import APIView

from apps.auth.serializers import LoginSerializer


class LoginView(APIView):

    def post(self, request):
        # serializer = LoginSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        return HttpResponse()
