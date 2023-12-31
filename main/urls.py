from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("create", views.create_item, name="Create Item"),
    path("edit/<int:id>", views.edit_item_view, name="Edit Item"),
    path("delete/<int:id>", views.delete_item_view, name="Delete Item"),

    path("items", views.get_items, name="Get Items"),
    path("items/<int:id>", views.get_item_by_id, name="Get Item by ID"),

    path("create-ajax", views.create_item_ajax, name="Create Item AJAX"),
    path('create-flutter/', views.create_product_flutter,
         name='create_product_flutter'),

    path("json", views.all_items_json, name="All Items JSON"),
    path("xml", views.all_items_xml, name="All Items XML"),
    path("json/<int:id>", views.items_by_id_json, name="Item by ID JSON"),
    path("xml/<int:id>", views.items_by_id_xml, name="Item by ID XML"),

    path("login", views.login_view, name="Login"),
    path("register", views.register_view, name="Register"),
    path("logout", views.logout_view, name="Logout"),
]
