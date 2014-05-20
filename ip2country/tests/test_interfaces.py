# -*- coding: utf-8 -*-

import unittest


class TestIStore(unittest.TestCase):

    @property
    def target(self):
        from ip2country.interfaces import IStore
        return IStore

    def make(self):
        return self.target()

    def test_persist(self):
        inst = self.make()

        with self.assertRaises(NotImplementedError):
            inst.persist('')

    def test_lookup(self):
        inst = self.make()

        with self.assertRaises(NotImplementedError):
            inst.lookup('', '')
