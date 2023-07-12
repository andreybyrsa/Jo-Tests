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