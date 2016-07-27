"""Test for djangopress.core.models."""
from model_mommy import mommy

from djangopress.core.models import Option


def test_option_str():
    """Test string representation for Option object."""
    option = mommy.prepare(Option)
    assert str(option) == option.name
