from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Укажите наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Модель",
        help_text="Укажите модель",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Продукт",
        blank=True,
        null=True,
        related_name="products",
    )
    foto = models.ImageField(
        upload_to="catalog/foto",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость"
    )
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, verbose_name="Скидка (%)"
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения", auto_now=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name

    def get_discounted_price(self):
        if self.discount:
            return self.price - (self.price * self.discount / 100)
        return self.price

    def get_full_description(self):
        return f"{self.name} - {self.category.name}: {self.description}" if hasattr(self, 'description') else self.name