from django.urls import path

from apps.manganelo_api.views import AnimeSearchView

urlpatterns = [
    path('', AnimeSearchView.as_view())
]
