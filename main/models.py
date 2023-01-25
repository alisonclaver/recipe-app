from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=1000)
    recipe_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name