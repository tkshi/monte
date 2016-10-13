from util import *
tehai = [[1, 1, 1, 0, 0, 0, 1, 1, 1],
         [0, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 2],
         ]

tehai = [[3, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 3, 0, 0, 3, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 0],
         [0, 2, 0],
         ]
set_pool = []

import itertools

for row_index,row in enumerate(tehai):
    for colum_index,cell in enumerate(row):
        if tehai[row_index][colum_index] >= 2:
            set_pool.append( ((row_index,colum_index),(row_index,colum_index)) )
        if tehai[row_index][colum_index] >= 3:
            set_pool.append( ((row_index,colum_index),(row_index,colum_index),(row_index,colum_index)) )
        if row_index <= 2 and colum_index <= 6 and tehai[row_index][colum_index] >= 1 and tehai[row_index][colum_index + 1] >= 1 and tehai[row_index][colum_index + 2] >= 1:
            set_pool.append( ((row_index,colum_index),(row_index,colum_index + 1),(row_index,colum_index + 2)) )

hand_list = list(itertools.combinations(set_pool,5))



def validCompleat(hand_list,tehai):
    filter_hand_list = filterToBeHaveSigleHead(hand_list)
    print("len(filter_hand_list)")
    print(filter_hand_list)
    print(len(filter_hand_list))
    return filterBeNotDuplicate(filter_hand_list,tehai)



result_hand_list = validCompleat(hand_list,tehai)

print(len(result_hand_list))
