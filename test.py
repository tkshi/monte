import unittest
from main import Hand
from monte import Monte

class TestStringMethods(unittest.TestCase):
    def test_check_hand_count(self):
        self.hand = Hand()
        hand_length = len(self.hand.getHand())
        self.assertEqual(hand_length, 3)
    def test_check_func(self):
        self.hand = Hand([1,2,7,8,9])
        result = self.hand.check()
        self.assertEqual(result, True)
    def test_playout(self):
        self.hand = Hand(initial=[1,2,7,8,9],mode="playout")
        result = self.hand.check()
        self.assertEqual(result, True)
    def test_playout_can_mulit_length(self):
        hand = Hand(initial=[1,2,7,8,9],mode="playout")
        hand.draw()
        hand.draw()
        hand.draw()
        result = hand.check()
        hand_length = len(hand.getHand())
    def test_get_cleared_array(self):
        hand = Hand(initial=[1,2,7,8,9,2,2],mode="playout")
        result = hand.get_cleared_part()
        self.assertEqual(len(result),3)
        self.assertEqual(int(result[0]),int(result[1]) - 1)
        self.assertEqual(int(result[1]),int(result[2]) - 1)
        self.assertEqual(int(result[0]),7)
        self.assertEqual(int(result[1]),8)
        self.assertEqual(int(result[2]),9)
    def test_montecalro(self):
        monte = Monte([1,9,8,3])
        monte.what_trash()
        self.assertEqual(monte.what_trash(),9)

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
