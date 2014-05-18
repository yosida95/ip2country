# -*- coding: utf-8 -*-

__all__ = ['IStore']


class IStore:

    def persist(self, record):
        raise NotImplementedError()

    def lookup(self, addr, type_):
        raise NotImplementedError
