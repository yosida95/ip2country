# -*- coding: utf-8 -*-

import bisect
from ip2country import (
    ipv4_to_bytes,
    ipv6_to_bytes,
    IStore,
)


class MemoryStore(IStore):

    def __init__(self):
        self.v4 = []
        self.v6 = []
        self.addr_to_record = {}

    def persist(self, record):
        if record.is_ipv6:
            bisect.insort(self.v6, record.start)
        else:
            bisect.insort(self.v4, record.start)

        self.addr_to_record[record.start] = record

    def lookup(self, addr, type_):
        if type_ == 'ipv4':
            addr = ipv4_to_bytes(addr)
            registry = self.v4
        elif type_ == 'ipv6':
            addr = ipv6_to_bytes(addr)
            registry = self.v6
        else:
            raise ValueError('Unknown type {0}'.format(type_))

        index = bisect.bisect(registry, addr)
        if index == 0:
            return None

        return self.addr_to_record[registry[index - 1]]
