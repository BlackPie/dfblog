from django.db import models
from django.utils.text import slugify


class Entry(models.Model):
    title = models.CharField(max_length=255)

    preview_text = models.TextField(blank=True,
                                    null=True)

    text = models.TextField(blank=True,
                            null=True)

    created = models.DateTimeField()

    image = models.ImageField(blank=True,
                              null=True)

    publish = models.BooleanField(default=True)

    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Entry, self).save()
