# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from utils.weixin.conf import get_conf

class CacheMixin(object):
    pass

class StateManager(object, CacheMixin):
    """
    只负责状态切换的逻辑，Cache封装在这一层。
    """

    def __init__(self, mapping, state=None):
        self.mapping = mapping
        self.use_cache = get_conf("WX_USE_CACHE")
        if self.use_cache:
            # 这里从cache中获取用户当前状态
            self.now_state = None
        else:
            # 否则根据分发来的状态制定初始状态
            self.now_state = state

    def get_state(self, input):
        next_state, kwargs = self.now_state.next(input)
        return self.mapping[next_state](**kwargs)

    def set_next(self, input):
        self.now_state = self.get_state(input)

    def handler(self, input):
        response = self.now_state.to_xml(input)
        self.set_next(input)
        return response