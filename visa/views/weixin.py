# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import View
from utils.weixin.receiver import WeiXinReceiver

class WeiXinInterfaceView(View):
    def get(self, request, *args, **kwargs):
        return None