#coding: utf-8

from django.core.paginator import Paginator as django_Paginator

class Paginator(object):
    _PAGE_SIZE_NOT_CARE = 1

    def __init__(self, data, total):
        self._data = data
        self._total = total
        self._page = None

        return

    def get_page(self):
        self._page = django_Paginator(self._data, self._PAGE_SIZE_NOT_CARE)
        self._page._count = self._total
        return  self._page

def new_page(data, total):return Paginator(data, total).get_page()
