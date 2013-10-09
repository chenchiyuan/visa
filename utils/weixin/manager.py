# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from utils.weixin.conf import get_conf
from utils.weixin.states import EchoState


class CacheMixin(object):
    def gen_cache_key(self, from_user_name, **kwargs):
        key = "USER:STATE:%s" % from_user_name
        return key

    def get_from_cache(self, from_user_name, **kwargs):
        from django.core.cache import cache
        key = self.gen_cache_key(from_user_name)
        return cache.get(key)

    def set_cache(self, from_user_name, **kwargs):
        from django.core.cache import cache
        key = self.gen_cache_key(from_user_name)
        cache.set(key, kwargs)

class StateManager(CacheMixin, object):
    """
    只负责状态切换的逻辑，Cache封装在这一层。
    """
    states = {
        "ECHO": EchoState,
    }


    def __init__(self, state_name, no_cache=False, **kwargs):
        # 如果no_cache, 默认不使用cache
        self.use_cache = get_conf("WX_USE_CACHE") and no_cache
        state = self.initial_state(state_name, **kwargs)
        if self.use_cache:
            # 这里从cache中获取用户当前状态
            self.now_state = None
        else:
            # 否则根据分发来的状态制定初始状态
            self.now_state = state

    @classmethod
    def initial(cls, state_name, **kwargs):
        state = cls.initial_state(state_name, **kwargs)
        return cls(state=state, no_cache=True, **kwargs)

    @classmethod
    def initial_state(cls, state_name, **kwargs):
        if not state_name in cls.states:
            return ""
        state_cls = cls.states[state_name]
        state = state_cls(**kwargs)
        return state

    def get_state(self, input):
        next_state, kwargs = self.now_state.next(input)
        return self.states[next_state](**kwargs)

    def set_next(self, input):
        self.now_state = self.get_state(input)

    def handler(self, input):
        response = self.now_state.to_xml(input)
        self.set_next(input)
        return response