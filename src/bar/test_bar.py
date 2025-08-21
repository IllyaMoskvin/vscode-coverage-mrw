import unittest

from bar import bar_method


class BarTestCase(unittest.TestCase):
    def test_bar(self):
        assert bar_method(True) is True
