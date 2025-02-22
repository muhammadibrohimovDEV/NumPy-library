# 8-dars . Arifmetik amallar

import numpy as np # kutubxonani chaqirib olish
arr1 = np.arange(6)
arr1 = arr1.reshape(2,3) # 0-5 (2,3) massiv

arr2 = np.arange(6 , 12)
arr2 = arr2.reshape(2 , 3) # 6-11 (2,3) maasiv

print(arr1 , "\n" ,  arr2)

# ko'paytirish
data1 = arr1 * arr2
print(data1) # mos indeksdagi elemntlar ko'paytmasi

# bo'lish
data2 = arr1 / arr2
print(data2) # mos indeksdagi elemntlar bo'linmasi

# qo'shish
data3 = arr1 + arr2
print(data3) # mos indeksdagi elemntlar yig'indisi

# ayrish
data4 = arr2 - arr1
print(data4) # # mos indeksdagi elemntlar ayrimasi

# darajaga oshirish
data5 = arr1**2 # massiv elemntlarini darajaga oshirish
print(data5)

# ildizdan chiqarish
data6 = arr2**0.5 # massiv elementlarini ma'lum darajadagi ildizdan chiqarish
print(data6)





