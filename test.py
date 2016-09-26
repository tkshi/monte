import unittest
from main import Hand

class TestStringMethods(unittest.TestCase):
    def test_check_hand_count(self):
        self.hand = Hand()
        hand_length = len(self.hand.getHand())
        self.assertEqual(hand_length, 3)
    def test_check_func(self):
        self.hand = Hand([1,2,7,8,8])
        result = self.hand.check()
        self.assertEqual(result, True)
  #
  # def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())
  #
  # def test_split(self):
  #     s = 'hello world'
  #     self.assertEqual(s.split(), ['hello', 'world'])
  #     # check that s.split fails when the separator is not a string
  #     with self.assertRaises(TypeError):
  #         s.split(2)

if __name__ == '__main__':
    unittest.main()
