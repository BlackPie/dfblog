from django.db import models


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
