import unittest

from path_finder import path_finder

class Tests(unittest.TestCase):

    def test1(self):
        """Check that a is not have exit"""
        a = "\n".join([
            ".W...",
            ".W...",
            ".W.W.",
            "...WW",
            "...W."])
        self.assertFalse(path_finder(a))