#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2017-12-10"


from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """

        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dic = {}
        #     json_dic["name"] = good.name
        #     json_dic["category"] = good.category.name
        #     json_dic["market_price"] = good.market_price
        #     json_dic["add_time"] = good.add_time
        #     json_list.append(json_dic)

        from django.forms.models import model_to_dict
        from django.http import HttpResponse, JsonResponse
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        from django.core import serializers
        import json
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)

