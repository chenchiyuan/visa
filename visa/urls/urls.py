# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.conf.urls import patterns, url
from visa.views.weixin import VisaResponseView


urlpatterns = patterns('',
   # url(r'^wx/v0/interface/$', WeiXinInterfaceView.as_view(), name="wx_interface"),
    url(r'^api/', VisaResponseView.as_view(), name="api"),
)