import json
from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.


@login_required(login_url='Login')
def index(request):
    items = Item.objects.filter(owner=request.user)
    context = {
        "name": request.user.username,
        "classOf": "D",
        "items": items,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)


@login_required(login_url='Login')
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return HttpResponseRedirect(reverse('Home'))
    else:
        form = ItemForm()
    return render(request, "create_item.html", {"name": request.user.username,
                                                "classOf": "D", "form": form})


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


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('Home'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(
                request, 'Sorry, incorrect username or password. Please try again.')
    return render(request, "login.html")


def register_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your account has been successfully created!')
            return HttpResponseRedirect(reverse('Login'))
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='Login')
def logout_view(request):
    logout(request)
    response = HttpResponseRedirect(reverse('Login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='Login')
def delete_item_view(request, id):
    # if (request.method == "DELETE"):
    item = Item.objects.get(pk=id, owner=request.user)
    if (item != None):
        item.delete()
        return HttpResponseRedirect(reverse('Home'))
    return HttpResponseRedirect(reverse('Edit Item', args=(id,)))


@login_required(login_url='Login')
def edit_item_view(request, id):
    item = Item.objects.get(pk=id, owner=request.user)
    if (item != None):
        if (request.method == "POST"):
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Home'))
        else:
            form = ItemForm(instance=item)
        return render(request, "edit_item.html", {"name": request.user.username,
                                                  "classOf": "D", "form": form, "id": id})
    return HttpResponseRedirect(reverse('Home'))


@login_required(login_url='Login')
def update_item_view(request, id):
    pass


def get_items(request):
    if request.user == None:
        return HttpResponseNotFound()
    items = Item.objects.filter(owner=request.user)
    return HttpResponse(serialize("json", items), content_type="application/json")


def get_item_by_id(request, id):
    if request.user == None:
        return HttpResponseNotFound()
    items = Item.objects.filter(owner=request.user, pk=id)
    return HttpResponse(serialize("json", items), content_type="application/json")


@csrf_exempt
def create_item_ajax(request):
    if request.user == None:
        return HttpResponseNotFound()
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount,
                           description=description, owner=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotAllowed()


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_product = Item.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
