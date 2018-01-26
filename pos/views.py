from django.http import JsonResponse
from django.shortcuts import render

from pos.models import Tag, ClothName


def home(request):
    return render(request, 'home.html')


def drop(request):
    return render(request, 'drop.html')


def get_tags(request):
    tags = Tag.objects.order_by('-used_count')
    resp = [{'name': tag.pinyin, 'id': tag.name} for tag in tags]
    return JsonResponse(resp, safe=False)


def get_cloth_names(request):
    names = ClothName.objects.order_by('-used_count')
    resp = [{'name': name.pinyin, 'id': name.name, 'price': name.price} for name in names]
    return JsonResponse(resp, safe=False)
