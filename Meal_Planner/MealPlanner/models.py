from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User
from users.models import MyUser


class Recipe(models.Model):
    recipe_id = models.IntegerField()
    recipe_name = models.CharField()

    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, related_name="favorite_recipes")

    def __str__(self):
        return self.recipe_name

