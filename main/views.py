from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        "name": "Maurice Yang",
        "classOf": "D",
        "items": items,
    }
    return render(request, "main.html", context)