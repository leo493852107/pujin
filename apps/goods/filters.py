#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-12-10"


import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    price_min = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # contains 区分大小写 / icontains 不区分大小写
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        # fields = ['price_min', 'price_max', 'name']
        fields = ['price_min', 'price_max']
