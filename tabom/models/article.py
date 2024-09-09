from django.db import models

from tabom.models.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=255)
