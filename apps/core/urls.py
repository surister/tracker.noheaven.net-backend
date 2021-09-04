from django.urls import path

from apps.core.views import AddAnime, GetAnime

urlpatterns = [
    path('add-anime/', AddAnime.as_view()),
    path('get-anime/', GetAnime.as_view()),
]
