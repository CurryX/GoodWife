import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from pos.models import Tag, ClothName, Order, OrderItem
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


def add_order(request):
    obj = json.loads(request.GET.get('order', ''))
    order = Order(total_price=obj['total'], cash_paid=obj['cash'], card_paid=obj['card'], discount=obj['discount'],
                  discount_percent=obj['discountPercent'], balance=obj['balance'], comment=obj['comment'])
    order.save()
    for item in obj['items']:
        order_item = OrderItem(name=item['name'], tags=item['tags'], unit_price=item['unitPrice'],
                             quantity=item['count'], comment=item['comment'], order=order)
        order_item.save()
    return JsonResponse({'id': order.pk})


def order_detail(request, id):
    order = get_object_or_404(Order, pk=id)
    items = OrderItem.objects.filter(order=order)
    return render(request, 'order.html', {'order': order, 'items': items, 'balance': abs(order.balance)})


def order_modify(request):
    order = get_object_or_404(Order, pk=request.GET.get('id', 0))
    action = request.GET.get('action', '')
    if action == 'complete':
        order.completed = True
        order.save()
    elif action == 'uncomplete':
        order.completed = False
        order.save()
    return HttpResponse()


def order_delete(request, id):
    order = get_object_or_404(Order, pk=id)
    order.delete()
    return redirect(reverse('home'))
