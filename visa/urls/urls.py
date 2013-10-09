# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.conf.urls import patterns, url
from visa.views.weixin import WeiXinInterfaceView


urlpatterns = patterns('',
    url(r'^wx/v0/interface/$', WeiXinInterfaceView.as_view(), name="wx_interface"),
)