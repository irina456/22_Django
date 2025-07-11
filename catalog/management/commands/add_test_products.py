from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Удаляет всё, затем добавляет тестовые продукты"

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write(self.style.WARNING("Все продукты и категории были удалены."))
        electronics = Category.objects.create(name='электроника', description='Электрокатегория')

        Product.objects.create(
            name="Nokia", description='Старое вечное', category=electronics, price=19000
        )

        Product.objects.create(
            name="Msi",
            description='Ноутбук современный',
            category=electronics,
            price=24000,
        )
        self.stdout.write(self.style.WARNING("Категория и продукты добавлены"))

