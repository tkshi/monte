#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Hand:
    hand = []
    def __init__(self):
        self.draw()
        self.draw()
        self.draw()
    def getHand(self):
        return self.hand
    def draw(self):
        if(len(self.hand) == 3):
            num = random.randint(1,9)
            self.hand.append(num)
            return self.hand
    def trash(self,num):
        if(len(self.hand) == 4):
            self.hand.remove(num)
    def check(self):
        prev_num = 0
        match_count = 0
        sorted_array = sorted(self.hand)
        result = False
        singled_array = list(set(sorted_array))
        for h in singled_array:

            if(prev_num == h - 1 and prev_num != 0):
                match_count = match_count + 1
                if(match_count == 2):
                    result = True
            else:
                match_count = 0
            prev_num = h
        return result

if __name__ == '__main__':
    hand = Hand()
    hand_array = hand.getHand()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.draw()
    hand.getHand()
    print(hand.check())
