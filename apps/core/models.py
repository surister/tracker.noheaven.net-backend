from django.contrib.auth.models import User
from django.db import models

from django.db.models import signals


def create_proxy_tracker_user(sender, instance, created, **kwargs):
    """Create ModelB for every new ModelA."""
    if created:
        Tracker.objects.create(user=instance)


class Tracker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.user}>'

    @property
    def animes(self):
        return Anime.objects.filter(tracker=self)


class Anime(models.Model):
    title = models.CharField(max_length=512)
    tracker = models.ManyToManyField(Tracker)

    def __str__(self):
        return self.title

    @property
    def sources(self):
        return Source.objects.filter(anime=self)


class Source(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.PROTECT)
    title = models.CharField(max_length=512)
    authors = models.CharField(max_length=256)
    views = models.IntegerField()
    last_updated = models.DateTimeField()


signals.post_save.connect(create_proxy_tracker_user, sender=User, weak=False,
                          dispatch_uid='models.create_proxy_tracker_user')
