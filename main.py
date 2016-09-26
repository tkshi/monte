#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Hand:
    hand = []
    def __init__(self,*args):
        if not len(args) == 1:
            self.draw()
            self.draw()
            self.draw()
        else:
            self.hand = args[0]
    def getHand(self):
        return sorted(self.hand)
    def draw(self):
        if(len(self.hand) <= 3):
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
                    result = True
            else:
                break
        return result

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
