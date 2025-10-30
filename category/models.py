from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="slug")
    description = models.TextField(blank=True, verbose_name="description")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
