from uuid import uuid4
from pytils.translit import slugify

def get_unique_slug(model, slug):
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{uuid4().hex[:8]}-{unique_slug}'
    return unique_slug