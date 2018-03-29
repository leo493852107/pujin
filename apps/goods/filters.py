#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-12-10"


import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # contains 区分大小写 / icontains 不区分大小写
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')


    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category=value))

    class Meta:
        model = Goods
        # fields = ['price_min', 'price_max', 'name']
        fields = ['pricemin', 'pricemax', 'is_hot']
