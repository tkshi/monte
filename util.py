def filterToBeHaveSigleHead(hand_list):
    _hand_list = hand_list[:]
    for hand in _hand_list:
        head_count = 0
        for _set in hand:
            if(len(_set) == 2):
                head_count = head_count + 1
        if(head_count != 1):
            hand_list.remove(hand)
    return hand_list
def filterBeNotDuplicate(hand_list,tehai):
    for hand in hand_list:
        head_count = 0
        for _set in hand:
            for s in _set:
                tehai[s[0]][s[1]] = tehai[s[0]][s[1]] - 1
                if tehai[s[0]][s[1]] == -1:
                    if(hand in hand_list):
                        hand_list.remove(hand)
    return hand_list
