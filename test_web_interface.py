import unittest


class TestModule(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    @unittest.skip("noreason")
    def test_fail(self):
        self.fail()
