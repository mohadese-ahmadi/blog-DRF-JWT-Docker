from .models import MenuItem


def menu_items(request):
    return {"menu_items": MenuItem.objects.filter(
        parent__isnull=True).prefetch_related("children")}
