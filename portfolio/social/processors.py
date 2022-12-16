from .models import Links


def ctx_dict(request):
    ctx = {}
    links = Links.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
