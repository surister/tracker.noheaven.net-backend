from django.urls import path

from apps.authentication.views import LoginView
from django.contrib.auth.views import LoginView as Lg

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('login2/', Lg.as_view())
]
