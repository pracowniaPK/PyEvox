from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Item
import json
import datetime


@csrf_exempt
def index(request):
    if request.method == "GET":
        if request.path_info == "/google/":
            return redirect("http://google.com/search?q={}".format(request.GET.get('co')))
        else:
            item_list = Item.objects.all()
            done_list = [
                len(item_list),
                len([i for i in item_list if i.done == True]),
                len([i for i in item_list if i.done == False]),
            ]
            context = {'item_list': item_list, 'done_list': done_list}
            return render(request, 'todos/todo_list.html', context)
    if request.method == "POST":
        json_data = json.loads(request.body)

        i = Item(title=json_data['title'])
        i.done = json_data['done'] if 'done' in json_data else False
        i.save()

        response_data = {"task_id": i.id}
        return JsonResponse(response_data)


@csrf_exempt
def item_details(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "GET":
        response_data = {
            "title": item.title,
            "done": item.done,
            "author_ip": item.author_ip,
            "created_date": item.created_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        return JsonResponse(response_data)
    if request.method == "PATCH":
        json_data = json.loads(request.body)
        print("{}|{}".format(item.title, item.done))
        if "title" in json_data:
            item.title = json_data["title"]
        if "done" in json_data:
            item.done = json_data["done"]
        print("{}|{}".format(item.title, item.done))
        item.save()

        return HttpResponse(status=204)
