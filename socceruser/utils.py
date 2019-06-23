import itertools
from django.utils.text import slugify
from oauth2_provider.models import AccessToken


def get_custom_slug(model, name, instance=None):
    slug = orig = slugify(name)
    instance_id = None
    if instance:
        instance_id = instance.id

    for x in itertools.count(1):
        if not model.objects.filter(slug=slug).exclude(pk=instance_id).exists():
            break
        slug = custom_slugify(orig, x)

    return slug


def custom_slugify(name, i=None):
    slug = slugify(name)
    if i is not None:
        slug += "-%d" % i
    return slug


def get_access_token(request):
    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    type_authorization, token = authorization_header.split()
    access_token = AccessToken.objects.get(token=token)
    return access_token
