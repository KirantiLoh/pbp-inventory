from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("create", views.create_item, name="Create Item"),

    path("json", views.all_items_json, name="All Items JSON"),
    path("xml", views.all_items_xml, name="All Items XML"),
    path("json/<int:id>", views.items_by_id_json, name="Item by ID JSON"),
    path("xml/<int:id>", views.items_by_id_xml, name="Item by ID XML"),
]