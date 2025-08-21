import unittest

from foo import foo_method


class FooTestCase(unittest.TestCase):
    def test_foo(self):
        assert foo_method(True) is True
