"""Context processors."""
from .models import Option

def settings(request):
    """Settings context_processor."""
    db_settings = {}
    settings = {
        'title': 'Just another blog',
    }
    options = Option.objects.all()
    for option in options:
        db_settings[option.name] = option.value
    settings.update(db_settings)
    return {'settings': settings}
