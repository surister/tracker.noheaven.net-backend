from django.urls import path

from apps.core.views import AddAnime

urlpatterns = [
    path('add-anime/', AddAnime.as_view())
]
