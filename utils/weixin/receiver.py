# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from conf import get_conf
from core import WeiXin

class WeiXinReceiver(object):
    """
    接受GET，POST的请求，进行参数校验。分发到对应的State
    """
    def __init__(self, user, request):
        self.user = user
        self.request = request

    def validate(self, token):
        return token == get_conf("WX_CONF")

    def dispatch(self):
        wx_object = WeiXin(xml_body=self.request.BODY, **self.request.GET)
        json_data = wx_object.to_json()
        msg_type = json_data.get("MsgType", "message")
        handler = getattr(self, msg_type, self.message)
        return handler(json_data)

    def message(self, json_data):
        return json_data

    def event(self, json_data):
        event = json_data['Event']
        if event == "subscribe":
            return json_data
        elif event == "unsubscribe":
            return json_data
        elif event == "CLICK":
            return json_data
        else:
            return json_data

    def image(self, json_data):
        return json_data

    def location(self, json_data):
        return json_data