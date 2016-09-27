#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main import Hand
hand = Hand(mode='playout')
while not hand.check():
    hand.draw()

class Monte:
    def __init__(self,hand):
        self.playout_count = 600
        self.origin_hand = hand
        self.hand = Hand(initial=self.origin_hand,mode='playout')
        self.score_dic = {}
    def playout(self):
        self.hand = Hand(initial=self.origin_hand[:],mode='playout')
        while not self.hand.check():
            self.hand.draw()
        comp_part = self.hand.get_cleared_part()
        self.set_score_dic(comp_part)
    def start_playout(self):
        for i in range(self.playout_count):
            self.playout()
    def set_score_dic(self,comp_parts):
        _origin_hand = self.origin_hand[:]
        for comp_part in comp_parts:
            for h in _origin_hand:
                if h in comp_part:
                    comp_part.remove(h)
                else:
                    self.score_dic[h] = self.score_dic.get(h,0) + 1
    def what_trash(self):
        self.start_playout()
        print(self.score_dic)
        ans = sorted(self.score_dic.items(), key=lambda x:x[1])[-1][0]
        return int(ans)

if __name__ == '__main__':
    monte = Monte([1,5,7])
    # monte.start_playout()
    print(monte.what_trash())
