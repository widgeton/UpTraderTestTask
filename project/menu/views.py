from django.shortcuts import render, HttpResponse
from django.db.models import Q
from . import models
from . import tree


def menus(request):
    objs = models.Menu.objects.all()
    context = {
        'menus': objs,
    }
    return render(request, 'menus.html', context)


def menu(request, pk):
    objs = models.Category.objects.filter(menu__pk=pk, parent__pk=None)
    cat_tree = tree.CategoryTree(objs)
    context = {
        'cats': cat_tree.roots,
    }
    return render(request, 'categories.html', context)


def categories(request, menu_pk, path):
    parent_ids = path.split('_')
    objs = models.Category.objects.filter(Q(parent__pk__in=parent_ids) | Q(parent__pk=None), menu__pk=menu_pk)
    cat_tree = tree.CategoryTree(objs)
    context = {
        'cats': cat_tree.roots
    }
    return render(request, 'categories.html', context)
