"""Test for djangopress.menus.models."""
from model_mommy import mommy

from djangopress.menus.models import Menu, MenuItem


def test_menu_str():
    """Test string representation for Menu object."""
    menu = mommy.prepare(Menu)
    assert str(menu) == menu.name


def test_menu_item_str():
    """Test string representation for MenuItem object."""
    item = mommy.prepare(MenuItem)
    assert str(item) == item.name


def test_menu_item_static_target():
    """Test menu item target when static url."""
    item = mommy.prepare(MenuItem)
    item.target = 'http://www.example.com'
    assert item.get_absolute_url() == 'http://www.example.com'
