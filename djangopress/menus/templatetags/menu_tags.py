"""Templatetags for menus."""
from django import template

from ..models import Menu


register = template.Library()


@register.inclusion_tag('menus/tags/menu.html')
def menu(menu_name):
    """Menu templatetag."""
    menu_object = Menu.objects.get(name=menu_name)
    items = menu_object.items.filter(parent__isnull=True)
    for item in items:
        item.show_dropdown = True if item.subitems.all() else False
    return {'menu_items': items}
