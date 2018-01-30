from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from pos.models import Tag, ClothName
from pos.pinyin import PinYin


pinyin = PinYin()
pinyin.load_word()


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


def update_frequency(request):
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            price = float(request.GET.get('price', '0'))
            if ClothName.objects.filter(name=name).exists():
                obj = ClothName.objects.get(name=name)
            else:
                obj = ClothName(name=name, pinyin=pinyin.hanzi2shouzimu(name), used_count=0, price=price)
            obj.used_count += 1
            obj.save()
    if 'tags' in request.GET:
        tags = request.GET['tags'].split('；')
        for tag in tags:
            if tag:
                if Tag.objects.filter(name=tag).exists():
                    obj = Tag.objects.get(name=tag)
                else:
                    obj = Tag(name=tag, pinyin=pinyin.hanzi2shouzimu(tag), used_count=0)
                obj.used_count += 1
                obj.save()
    return HttpResponse()
