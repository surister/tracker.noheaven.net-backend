import manganelo.rewrite as manganelo

results = manganelo.search(title='Naruto')

for r in results:
    print(dir(r))
    print(r.title)
    print(r.icon_url)
    print(r.url)
    print(r.updated)
    print(r.views)
    print(r.rating)
    print(r.authors)

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_soup', 'authors', 'chapter_list', 'download_icon', 'icon_url', 'rating', 'title', 'updated', 'url', 'views']