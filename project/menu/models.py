from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=256)
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
