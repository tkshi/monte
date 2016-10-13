def filterToBeHaveSigleHead(hand_list):
    for hand in hand_list:
        head_count = 0
        for _set in hand:
            if(len(_set) == 2):
                head_count = head_count + 1
        if(head_count != 1):
            hand_list.remove(hand)
    return hand_list
