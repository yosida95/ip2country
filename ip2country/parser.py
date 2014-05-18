# -*- coding: utf-8 -*-

from .record import (
    Metadata,
    Record,
)

__all__ = ['Parser']


class Parser:

    def __init__(self, store):
        self.store = store

    def parse_record(self, metadata, line):
        factors = line.split('|')
        if len(factors) < 7:
            return

        registry, cc, type_, start, value, dete, status = factors[:7]
        if type_ not in ('ipv4', 'ipv6'):
            return

        return Record(metadata, start, type_, value, cc)

    def do(self, fp):
        metadata = None
        for line in fp:
            line = line[:-1]

            if line.startswith('#') or line.endswith('summary'):
                continue

            if metadata is None:
                version, registry, serial, records,\
                    startdate, enddate, utcoffset = line.split('|')[:7]
                metadata = Metadata(registry, version, serial)
                continue

            record = self.parse_record(metadata, line)
            if record is None:
                continue

            self.store.persist(record)
