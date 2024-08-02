#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .common import EchoFactory, Request, BaseUnitTest
import unittest

HTTP_METHODS = [b"OPTIONS", b"HEAD", b"GET", b"POST", b"PUT", b"DELETE"]

class ProtocolUnitTest(BaseUnitTest):
    __name__ = 'ProtocolUnitTest'
    methods = [b"OPTIONS"]

    # Skip this test because it seems to be testing Twisted rather than
    # txsockjs, and it doesn't currently work.
    @unittest.skip
    def test_405(self):
        methods = list(set(HTTP_METHODS).difference(set(self.methods)))
        for m in methods:
            self.request.method = m
            self._load()
            self.assertEqual(self.request.responseCode, 405)
            self.assertFalse(self.request.responseHeaders.hasHeader(b"content-type"))
            self.assertTrue(self.request.responseHeaders.hasHeader(b"allow"))
            self.assertFalse(self.request.value())