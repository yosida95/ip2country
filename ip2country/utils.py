# -*- coding: utf-8 -*-

__all__ = ['ipv4_to_bytes', 'ipv6_to_bytes']


def ipv4_to_bytes(ip):
    return bytes(int(part) for part in ip.split('.'))


def ipv6_to_bytes(ip):
    parts = ip.split(':')
    length = len(parts)
    if length < 8:
        index = parts.index('')
        if index == 0:
            parts[0] = '0'
            index += 1

        parts =\
            parts[:index] + list('0' * (7 - index)) + parts[index + 1:]

        if parts[-1] == '':
            parts[-1] = '0'

        assert len(parts) == 8

    return b''.join(
        bytes([int(part[-4:-2] or '0', 16), int(part[-2:], 16)])
        for part in parts
    )
