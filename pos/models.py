from django.db import models


class Member(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    pinyin = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    balance = models.FloatField()
    discount = models.FloatField()
    comment = models.TextField()


class Order(models.Model):
    member = models.ForeignKey(Member, related_name='orders', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    total_price = models.FloatField()
    cash_paid = models.FloatField()
    card_paid = models.FloatField()
    discount = models.FloatField()
    discount_percent = models.FloatField()
    balance = models.FloatField()
    all_washed = models.BooleanField(default=False)
    all_picked = models.BooleanField(default=False)
    comment = models.TextField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    name = models.TextField()
    tags = models.TextField()
    washed = models.BooleanField(default=False)
    picked = models.BooleanField(default=False)
    unit_price = models.FloatField()
    quantity = models.FloatField()
    comment = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=40)
    pinyin = models.CharField(max_length=40)
    used_count = models.IntegerField()


class ClothName(models.Model):
    name = models.CharField(max_length=40)
    pinyin = models.CharField(max_length=40)
    used_count = models.IntegerField()
    price = models.FloatField()
