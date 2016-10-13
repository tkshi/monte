tehai = [[3, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 2, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 0, 0, 1, 1],
         [3, 0, 1, 1],
         [1, 1, 1],
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
print(len(set_pool))
print(list(itertools.combinations(set_pool,5)))
# print(set_pool)
