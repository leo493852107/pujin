#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "leo"
__time__ = "2018-03-25"


import requests
import json


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【彩色灯具】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(url=self.single_send_url, data=params)
        res_dic = json.loads(response.text)
        return res_dic


if __name__ == '__main__':
    yun_pian = YunPian("87dc988ce49b65088687dc21ad007465")
    yun_pian.send_sms('2018', '18395960706')

