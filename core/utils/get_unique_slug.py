from uuid import uuid4
from pytils.translit import slugify

def get_unique_slug(model, slug):
    if len(slug) == 0:
        unique_slug = uuid4().hex[:20]
    else:
        unique_slug = slugify(slug)[:60] + '-' + uuid4().hex[:20]
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug[:60]}-{uuid4().hex[:20]}'
    return unique_slug

def get_unique_index(model, index):
    if len(index) == 0:
        unique_index = uuid4().hex[:20]
    else:
        unique_index = slugify(index)[:60] + '-' + uuid4().hex[:20]
    while model.objects.filter(index=unique_index).exists():
        unique_index = f'{unique_index[:60]}-{uuid4().hex[:20]}'
    return unique_index