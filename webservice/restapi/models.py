from django.db import models


class Answer(models.Model):
    jsonfield = models.TextField(blank=True)

    def __str__(self):
        return self.jsonfield
