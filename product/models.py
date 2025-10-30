from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    description = models.TextField(verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    stock = models.PositiveIntegerField(verbose_name="stock")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="category",
    )
    image = models.ImageField(
        upload_to="products/%Y/%m/%d/", blank=True, null=True, verbose_name="image"
    )

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.stock > 0
