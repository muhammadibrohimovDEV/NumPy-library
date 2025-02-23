# 11-dars . Takrorlanmas va boshqa amallar

import numpy as np # kutubxonani chaqirib olish

# data
names = np.array(['Sarvar', 'Abdurahmon', 'Hasan',  'Temur', 'Sarvar', 'Temur'])
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])

# unique - takrorlanmas elemntlarni qaytaradi , takrorlansa ham faqat bittasini qabul qiladi
unique_names = np.unique(names) # set kabi
print(unique_names)

unique_ints = np.unique(ints)
print(unique_ints)

set_names = set(names)
print(set_names)

# isin - ikki argument qabul qiladi , 2-massivning har bir elementini boshqa massivda borligini tekshiradi , bor bo'lsa True , yo'q bo'lsa False
arr1 = np.array([6, 0, 0, 3, 2, 5, 6])
arr2 = np.array([0, 2, 3])

arr3 = np.isin(arr1 , arr2)
print(arr3)

# setdiff1d - ikki argument qabul qiladi , 2-massivning har bir elementini boshqa massivda borligini tekshiradi , yo'q bo'lganini qaytaradi
names1 = np.array(['Jasur', 'Abdurahmon', 'Hasan',  'Muhammad', 'Sarvar', 'Temur'])
names2 = np.array(['Sarvar', 'Abdurahmon', 'Hasan',  'Temur', 'Sarvar', 'Temur'])

names3 = np.setdiff1d(names1 , names2)
print(names3)

