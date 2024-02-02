from django.core.management import BaseCommand
from menu import models


class Command(BaseCommand):
    help = 'Создает тестовые Меню и Категории с подкатегориями'

    def handle(self, *args, **options):
        for i in range(1, 4):
            menu = models.Menu(name=f'Меню {i}')
            menu.save()
            for j in range(1, 4):
                name = f'Категория {j}'
                cat = models.Category(name=name, parent=None, menu=menu)
                cat.save()
                self._set_categories(4, name, menu, cat)

    def _set_categories(self, depth: int, name: str, menu: models.Menu, parent: models.Category):
        if depth <= 0:
            return
        for i in range(1, 4):
            new_name = f'{name}.{i}'
            cat = models.Category(name=new_name, parent=parent, menu=menu)
            cat.save()
            self._set_categories(depth-1, new_name, menu, cat)
