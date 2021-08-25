from rest_framework.response import Response
from rest_framework.views import APIView

import manganelo.rewrite as manganelo


class AnimeSearchView(APIView):
    def get(self, request):
        data = []
        print(self.kwargs)
        results = manganelo.search(title=request.GET.get('search'))

        for i, r in enumerate(results):
            k = {
                'id': i,
                'title': r.title,
                'img': r.icon_url,
                'authors': ", ".join(r.authors),
                'ratings': r.rating,
                'updated': r.updated,
                'views': r.views,
                'url': r.url
            }
            data.append(k)

        return Response(data)
