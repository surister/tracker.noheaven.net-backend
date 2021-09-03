from django.urls import path

from apps.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView)
]
