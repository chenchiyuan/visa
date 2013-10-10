# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from interface import StateInterface

class EchoState(StateInterface):
    def next(self, input):
        state, kwargs = super(EchoState, self).next(input)
        return "ECHO", kwargs

    def to_xml(self, input):
        return self._to_wx_text(input)


class VideoState(StateInterface):
    def next(self, input):
        state, kwargs = super(VideoState, self).next(input)
        return "ECHO", kwargs

    def to_xml(self, input):
        content = "http://v.youku.com/v_show/id_XNjE5NTM3MTE2.html?f=20330711&ev=2"
        return self._to_wx_text(content)