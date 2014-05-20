# -*- coding: utf-8 -*-

import sys
if sys.version_info[0] >= 3:
    strtype = str
else:
    strtype = unicode
import unittest
try:
    from unittest import mock
except ImportError:
    import mock

try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO


class ParserTest(unittest.TestCase):

    @property
    def target(self):
        from ip2country.parser import Parser
        return Parser

    def make(self, store):
        return self.target(store)

    def test_constructor(self):
        store = object()

        inst = self.make(store)
        self.assertIs(inst.store, store)

    def test_parse_record(self):
        metadata = object()
        inst = self.make(object())

        with mock.patch('ip2country.parser.Record') as m:
            inst.parse_record(
                metadata,
                'apnic|JP|ipv4|133.0.0.0|16777216|19970301|allocated')

            m.assert_call_once_with(
                metadata, 'apnic', '133.0.0.0', 'ipv4', '1677216', 'JP')

    def test_parse_record_unknown_type(self):
        inst = self.make(object())

        record = inst.parse_record(
            object(),
            'apnic|JP|ipv5|133.0.0.0|16777216|19970301|allocated')
        self.assertIsNone(record)

    def test_parse_not_record(self):
        inst = self.make(object())

        record = inst.parse_record(object(), 'apnic|*|asn|*|5693|summary')
        self.assertIsNone(record)

    def test_do(self):
        fp = StringIO()
        fp.write('\n'.join(map(
            lambda line: strtype(line),
            [
                '# comment line',
                '2|apnic|20140519|32559|19850701|20140516|+1000',
                'apnic|*|ipv4|*|1|summary',
                'apnic|JP|ipv4|133.0.0.0|16777216|19970301|allocated',
            ]
        )))
        fp.seek(0)

        store = mock.Mock()
        inst = self.make(store)
        inst.parse_record = mock.Mock()
        with mock.patch('ip2country.parser.Metadata') as metadata:
            inst.do(fp)

            metadata.assert_call_once_with('apnic', '2', '20140519')

            self.assertEqual(inst.parse_record.call_count, 1)
            inst.parse_record.assert_call_once_with(
                metadata(),
                'apnic|JP|ipv4|133.0.0.0|16777216|19970301|allocated')

            self.assertEqual(store.persist.call_count, 1)

    def test_do_with_invalid_record(self):
        fp = StringIO()
        fp.write('\n'.join(map(
            lambda line: strtype(line),
            [
                '# comment line',
                '2|apnic|20140519|32559|19850701|20140516|+1000',
                'apnic|*|ipv5|*|1|summary',
                'apnic|JP|ipv5|133.0.0.0|16777216|19970301|allocated',
            ],
        )))
        fp.seek(0)

        store = mock.Mock()
        inst = self.make(store)
        inst.parse_record = mock.Mock(return_value=None)
        with mock.patch('ip2country.parser.Metadata') as metadata:
            inst.do(fp)

            metadata.assert_call_once_with('apnic', '2', '20140519')

            self.assertEqual(inst.parse_record.call_count, 1)
            inst.parse_record.assert_call_once_with(
                metadata(),
                'apnic|JP|ipv5|133.0.0.0|16777216|19970301|allocated')

            self.assertEqual(store.persist.call_count, 0)
