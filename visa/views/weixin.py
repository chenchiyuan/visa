# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from utils.weixin.receiver import WeiXinReceiver
from django.http import HttpResponse

class WeiXinInterfaceView(View):
    def get(self, request, *args, **kwargs):
        receiver = WeiXinReceiver(request)
        return HttpResponse(receiver.echo())

    def post(self, request, *args, **kwargs):
        receiver = WeiXinReceiver(request)
        return HttpResponse(receiver.dispatch())

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WeiXinInterfaceView, self).dispatch(request, *args, **kwargs)