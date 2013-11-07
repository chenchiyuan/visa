# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from utils.weixin.receiver import WeiXinReceiver
from django.http import HttpResponse
from visa.models import Visa


import json

def json_response(json_data, **kwargs):
    data = json.dumps(json_data)
    return HttpResponse(data, content_type='application/json', **kwargs)


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


class VisaResponseView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VisaResponseView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query", "")
        data = Visa.response_query(query)
        return json_response(data)