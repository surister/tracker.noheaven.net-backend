from django.contrib.auth.models import User
from django.db import models

from django.db.models import signals


def create_proxy_tracker_user(sender, instance, created, **kwargs):
    """Create ModelB for every new ModelA."""
    if created:
        Tracker.objects.create(user=instance)


class Anime(models.Model):
    title = models.CharField(max_length=512)

    def __str__(self):
        return self.title

    @property
    def sources(self):
        return Source.objects.filter(anime=self)


class Tracker(models.Model):
    """
    Proxy model that connects:

    User 1:1 Tracker 1:m AnimeProfiles

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.user}>'

    @property
    def animes(self):
        return AnimeProfile.objects.filter(tracker=self)


class AnimeProfile(models.Model):
    tracker = models.ForeignKey(Tracker, on_delete=models.PROTECT)
    anime = models.ForeignKey(Anime, on_delete=models.PROTECT)
    last_time_read = models.DateTimeField(null=True, blank=True)
    current_chapter = models.CharField(default='1', max_length=120)

    def __str__(self):
        return f'{str(self.tracker)} - {str(self.anime)}'


class Source(models.Model):
    class SourceChoices(models.TextChoices):
        custom = 1, 'Manganelo'
        manganelo = 2, 'Manganelo'

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    chapter_count = models.FloatField()
    title = models.CharField(max_length=512)
    type = models.CharField(choices=SourceChoices.choices, max_length=30)
    image = models.URLField()
    authors = models.CharField(max_length=256)
    views = models.IntegerField()
    last_updated = models.DateField()


signals.post_save.connect(create_proxy_tracker_user, sender=User, weak=False,
                          dispatch_uid='models.create_proxy_tracker_user')
