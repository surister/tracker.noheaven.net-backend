from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

import manganelo.rewrite as manganelo


class AnimeSearchView(APIView):
    def get(self, request):
        data = []
        results = manganelo.search(title=request.GET.get('search'))

        for i, r in enumerate(results):
            k = {
                'search_id': i,
                'title': r.title,
                'img': r.icon_url,
                'authors': ", ".join(r.authors),
                'ratings': r.rating,
                'updated': r.updated.date(),
                'views': r.views,
                'url': r.url,
                'chapters_length': len(r.chapter_list())

            }
            data.append(k)

        title_list = [i.get('title') for i in data]

        animes_user_already_have = User.objects.get(id=3).tracker.animes.filter(title__in=title_list)

        for anime in data:
            anime_match = animes_user_already_have.filter(title__icontains=anime['title'])
            anime['user_has_it'] = anime_match.exists()

        return Response(data)
