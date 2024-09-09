from django.db import models

from tabom.models.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=50)
