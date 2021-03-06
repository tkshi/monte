#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Hand:
    hand = []
    def __init__(self,initial=[random.randint(1,9),random.randint(1,9),random.randint(1,9)],mode="Normal"):
        self.mode = mode
        self.hand = initial[:]
        self.matched_tunks = []
    def getHand(self):
        return sorted(self.hand)
    def draw(self):
        if(len(self.hand) <= 3 or self.mode is 'playout'):
            num = random.randint(1,9)
            self.hand.append(num)
            return self.hand
    def trash(self,num):
        if(len(self.hand) == 4):
            self.hand.remove(num)
    def check(self):

        prev_num = 0
        match_count = 0
        singled_array = list(set(self.hand))
        singled_array = sorted(singled_array)
        result = False
        hand_length = len(singled_array)
        for i in range(0,hand_length):
            if(i + 2 < hand_length):
                if singled_array[i] == singled_array[i + 1] -1 == singled_array[i + 2] -2:
                    self.matched_tunks.append([singled_array[i],singled_array[i+1],singled_array[i+2]])
                    result = True
            else:
                break
        return result
    def get_cleared_part(self):
        self.check()
        return self.matched_tunks

if __name__ == '__main__':
    hand = Hand()
    hand.getHand()
    success = False
    while not success:
        hand.draw()
        print(hand.check())
        if hand.check() is True:
            success = True
            break
        print(hand.getHand())
        print("なにを切りますか？")
        num = raw_input()
        hand.trash(int(num))
    print(hand.getHand())
    print("成功です")
