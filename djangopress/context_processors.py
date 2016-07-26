"""Context processors."""
from .models import Option


def settings(request):  # pylint: disable=unused-argument
    """Settings context_processor."""
    db_settings = {}
    default_settings = {
        'title': 'Just another blog',
        'tagline': '',
    }
    options = Option.objects.all()
    for option in options:
        db_settings[option.name] = option.value
    default_settings.update(db_settings)
    return {'settings': default_settings}
