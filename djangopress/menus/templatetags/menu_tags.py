"""Templatetags for menus."""
from django import template

from ..models import Menu


register = template.Library()


@register.inclusion_tag('menus/tags/menu.html')
def menu(menu_name):
    """Menu templatetag."""
    menu_object = Menu.objects.get(name=menu_name)
    return {'menu_items': menu_object.menuitem_set.all()}
