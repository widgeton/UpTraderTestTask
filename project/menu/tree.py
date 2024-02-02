from . import models
from typing import Sequence


class CategoryTree:
    def __init__(self, categories: Sequence[models.Category]):
        self.roots = []
        self._cats = {cat.pk: _Category(cat) for cat in categories}
        self._build_tree()
        self._set_paths()

    def _build_tree(self):
        for cat in self._cats.values():
            if cat.parent_id in self._cats:
                self._cats[cat.parent_id].children.append(cat)
            elif cat.parent_id is None:
                self.roots.append(cat)

    def _set_paths(self):
        for cat in self._cats.values():
            ancs = self.get_all_ancestors(cat.id)
            anc_ids = [str(anc.id) for anc in reversed(ancs)]
            anc_ids.append(str(cat.id))
            cat.path = '_'.join(anc_ids)

    def get_all_ancestors(self, cat_id):
        ancestors = []
        cat = self._cats[cat_id]
        while cat.parent_id is not None:
            cat = self._cats[cat.parent_id]
            ancestors.append(cat)
        return ancestors


class _Category:
    def __init__(self, category: models.Category):
        self.id = category.pk
        self.name = category.name
        self.parent_id = category.parent_id
        self.menu_id = category.menu_id
        self.path = None
        self.children = []

    def has_children(self):
        return len(self.children) > 0
