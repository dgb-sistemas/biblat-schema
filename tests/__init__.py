import unittest


def discover_suite():
    # https://docs.python.org/2/library/unittest.html#unittest.TestLoader.discover
    return unittest.defaultTestLoader.discover('.', pattern='test_*.py')
