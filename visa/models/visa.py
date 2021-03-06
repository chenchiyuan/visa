# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.db.models import Q
import json


class QuerysetMixin(object):
    @classmethod
    def get_by_unique(cls, **kwargs):
        try:
            instance = cls.objects.get(**kwargs)
        except Exception, err:
            print(err)
            instance = None
        return instance

    @classmethod
    def get_by_queries(cls, **kwargs):
        query_list = [Q(**{key: value}) for key, value in kwargs.items()]
        query = query_list.pop()
        for query_append in query_list:
            query &= query_append

        try:
            item = cls.objects.get(query)
        except Exception:
            item = None
        return item

    @classmethod
    def filter_by_queries(cls, **kwargs):
        query_list = [Q(**{key: value}) for key, value in kwargs.items()]
        query = query_list.pop()
        for query_append in query_list:
            query &= query_append

        try:
            item = cls.objects.filter(query)
        except Exception:
            item = None
        return item


class Visa(models.Model, QuerysetMixin):

    class Meta:
        app_label = "visa"
        db_table = "visa_visa"
        verbose_name = verbose_name_plural = u"签证"

    name = models.CharField(u"签证名", max_length=32, db_index=True)
    category = models.CharField("类别", max_length=32, blank=True, null=True, default="")
    price = models.CharField("价格", max_length=32, blank=True, null=True, default="")

    content = models.TextField(u"内容", max_length=4096, blank=True)

    def __unicode__(self):
        return "%s签证, 价格:%s, 类别: %s" %(self.name, self.price, self.category)

    def to_article(self):
        return {
            "title":  unicode(self),
            "description": "价格: %s, 类别: %s" %(self.price, self.category),
            "picurl": "http://www.ailvxing.com/d/file/travel-info/visanews/Africa/2010-09-08/a1efe12058da663548f2f0f6d82da641.png",
            "url": self.url,
        }

    @property
    def url(self):
        json_data = json.loads(self.content)
        return json_data.get("url", "")

    @classmethod
    def response_query(cls, query):
        query = query.replace("签证", "")
        visas = cls.filter_by_queries(name=query)

        articles = []
        for visa in visas[:10]:
            articles.append(visa.to_article())
        return articles