# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^wx/v0/interface/$', include('visa.urls.urls'),),
)