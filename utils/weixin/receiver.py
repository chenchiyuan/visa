# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from conf import get_conf
from core import WeiXin
from manager import StateManager

class WeiXinReceiver(object):
    """
    接受GET，POST的请求，进行参数校验。分发到对应的初始State
    """
    def __init__(self, request):
        self.request = request

    def echo(self):
        return self.request.GET.get("echostr", "")

    def validate(self, token):
        return token == get_conf("WX_CONF")

    def dispatch(self):
        wx_object = WeiXin(xml_body=self.request.body, **self.request.GET)
        json_data = wx_object.to_json()
        msg_type = json_data.get("MsgType", "message")
        handler = getattr(self, msg_type, self.message)
        return handler(json_data)

    def message(self, json_data):
        manager = StateManager(state_name="VIDEO", **json_data)
        return manager.handler(json_data.get("content", ""))
    #
    #def event(self, json_data):
    #    event = json_data['Event']
    #    if event == "subscribe":
    #        return json_data
    #    elif event == "unsubscribe":
    #        return json_data
    #    elif event == "CLICK":
    #        return json_data
    #    else:
    #        return json_data
    #
    #def image(self, json_data):
    #    return json_data
    #
    #def location(self, json_data):
    #    return json_data
