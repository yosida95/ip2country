# -*- coding: utf-8 -*-

import os.path
import socket

from ip2country import Parser
from store import MemoryStore


def load(store):
    parser = Parser(store)

    for name in ('afrinic', 'apnic', 'arin', 'iana', 'lacnic', 'ripe'):
        with open(os.path.join('./data', name), 'r') as fp:
            parser.do(fp)


def main():
    store = MemoryStore()
    load(store)

    for host in ('www.google.com', 'www.amazon.com'):
        print('{0}: {1}'.format(
            host, store.lookup(socket.gethostbyname(host), 'ipv4').cc
        ))


if __name__ == '__main__':
    main()
