# -*- coding: utf-8 -*-

from nose.tools import eq_

from ip2country import (
    ipv4_to_bytes,
    ipv6_to_bytes,
)


def test_ipv4_to_bytes():
    eq_(ipv4_to_bytes('1.2.3.4'), b'\x01\x02\x03\x04')


def test_ipv6_to_bytes():
    eq_(ipv6_to_bytes('::1'), b'\x00' * 14 + b'\x00\x01')
    eq_(ipv6_to_bytes('1::'), b'\x00\x01' + b'\x00' * 14)
    eq_(ipv6_to_bytes('1::1'), b'\x00\x01' + b'\x00' * 12 + b'\x00\x01')
    eq_(ipv6_to_bytes('01:23:45:67:89:fafb:fcfd:feff'),
        b'\x00\x01\x00\x23\x00\x45\x00\x67\x00\x89\xfa\xfb\xfc\xfd\xfe\xff')
