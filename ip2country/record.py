# -*- coding: utf-8 -*-

from .utils import (
    ipv4_to_bytes,
    ipv6_to_bytes,
)

__all__ = ['Metadata', 'Record']


class Metadata:

    def __init__(self, registry, version, serial):
        self.registry = registry
        self.version = version
        self.serial = serial


class Record:

    def __init__(self, metadata, start, type_, value, cc):
        self.metadata = metadata
        self.start_h = start
        self.value = value
        self.cc = cc

        if type_ == 'ipv4':
            self.start = ipv4_to_bytes(start)
        elif type_ == 'ipv6':
            self.start = ipv6_to_bytes(start)
        else:
            raise ValueError('Unknown type: {0}'.format(type_))

    @property
    def is_ipv6(self):
        return len(self.start) == 16

    def __repr__(self):
        return '<Record: {0}>'.format(self.start_h)

    def __str__(self):
        return self.__repr__()
