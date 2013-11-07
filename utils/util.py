# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from bs4 import BeautifulSoup
from visa.models import Visa
import requests
import json


url = "http://www.ailvxing.com/qunar.xml"


def get_ailvxing():
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content)

    items = soup.find_all("item")
    result = []

    for item in items:
        base = item.attrs
        base['confine'] = item.find("confine").text
        base['url'] = item.find("url").text
        result.append(base)
    return result


def to_db():
    items = get_ailvxing()
    for item in items:
        name = item['country']
        category = item['category']
        price = item['price']

        content = json.dumps(item)
        v = Visa(name=name, category=category, price=price, content=content)
        v.save()



