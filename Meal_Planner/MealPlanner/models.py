from django.db import models
from django.contrib.auth.models import User
from users.models import MyUser
from jsonfield import JSONField

class Recipe(models.Model):
    recipe_id = models.IntegerField()
    recipe_name = models.CharField(max_length=200)

    recipe_info = JSONField(null=True)


    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, related_name="favorite_recipes")

    def __str__(self):
        return self.recipe_name

