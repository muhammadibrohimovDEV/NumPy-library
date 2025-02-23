# 10-dars . Tartiblsh (Sorting)

import numpy as np # kutubxonani chaqirib oldik

# data
arr = np.random.rand(4) # 4 elementli massiv
print(arr)

# sort metodi
arr_sorted = np.sort(arr) # o'sish ketma-ketligida saralash . 1-usul
arr.sort() # 2-usul

print(arr)
print(arr_sorted)

# teskari tartiblash
arr_reversed_sorted = -np.sort(-arr) # teskari tartibdagi saralash
print(arr_reversed_sorted)


# 2d massiv
arr2d = np.random.randn(2,4) # (2 , 4) random massiv
print(arr2d)

# axis = 0 satr
# axis = 1 ustun
row_sorted = np.sort(arr2d , axis = 0)
column_sorted = np.sort(arr2d , axis = 1)

print(row_sorted , "\n" , column_sorted)



