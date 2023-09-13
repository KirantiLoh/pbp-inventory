from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.serializers import serialize
# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        "name": "Maurice Yang",
        "classOf": "D",
        "items": items,
    }
    return render(request, "main.html", context)

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Home'))
    else:
        form = ItemForm()
    return render(request, "create_item.html", {"name": "Maurice Yang",
        "classOf": "D","form": form})

def all_items_json(request):
    items = Item.objects.all()
    return HttpResponse(serialize("json", items), content_type="application/json")

def all_items_xml(request):
    items = Item.objects.all()
    return HttpResponse(serialize("xml", items), content_type="application/xml")

def items_by_id_json(request, id):
    item = Item.objects.filter(pk=id)
    return HttpResponse(serialize("json", item), content_type="application/json")

def items_by_id_xml(request, id):
    item = Item.objects.filter(pk=id)
    return HttpResponse(serialize("xml", item), content_type="application/xml")