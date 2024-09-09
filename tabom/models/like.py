from django.db import models

from tabom.models.article import Article
from tabom.models.models import BaseModel
from tabom.models.user import User


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "article"], name="unique_user_article"),
        ]

    @classmethod
    def do_like(cls, user_id: int, article_id: int) -> "Like":
        return Like.objects.create(user_id=user_id, article_id=article_id)
