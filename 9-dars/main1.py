# 9-dars . Matematik va Statistik amallarni qo'llash

import numpy as np # kutubxonani chqirib olamiz

arr = np.random.randn(5 , 4) # (5 , 4) o'lchovli massiv
print(arr)

# sum metodi
data1 = np.sum(arr) # massivdagi barcha elemntlarini yig'indisini hisoblab beradi
data = arr.sum()
print(data1)

data_satr = arr.sum(axis=1) # satr yig'indisi
print(data_satr)

data_ustun = arr.sum(axis=0) # ustun yig'indisi
print(data_ustun)

# sodda ma'lumot
arr2 = np.arange(5) # 0 dan 5 gacha tashkil topgan massiv
print(arr2)

# mean metodi
data2 = arr2.sum() / np.size(arr2)
print(data2)

data2 = arr2.mean() # massiv elemntlarining o'rta arifmetgini qaytaradi
print(data2)

print(arr.mean(axis=1)) # har bir satr o'rta arifmetigi np.mean(arr , axis=1)
print(arr.mean(axis=0)) # har bir ustun o'rta arifmetigi np.mean(arr , axis=0)

# cumsum
print(np.cumsum(data2)) # massivning har bir elemntlarini elemtngacha bo'lgan yig'indilarga qo'shib hisoblaydi

# cumprod
print(np.cumprod(data2)) # massivning har bir elemntlarini elemtngacha bo'lgan kopaytmalarga ko'paytiriv hisoblaydi

# std , var
print(arr.std()) # standart og'ish
print(arr.std(axis = 1)) # massivning har bir satrining standart og'ishi
print(arr.std(axis = 0)) # massivning har bir ustunining standart og'ishi

print(arr.var()) # variatsiya
print(arr.var(axis = 1)) # massivning har bir satrining variatsiyasi
print(arr.var(axis = 0)) # massivning har bir ustunining variatsiyasi





