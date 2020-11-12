import unittest
from kaya_identity import calculate_score

class TestKayaCompute(unittest.TestCase):

    def test_accuracy(self):
        self.assertEqual(calculate_score(82.4, 44, 5, 0.05), 44)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()