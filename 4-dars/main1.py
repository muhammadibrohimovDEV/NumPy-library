import numpy as np # kutubonani chaqirib olish

# 4-dars . NumPy kutubxonasida Boolean (True or False) indekslash va kesish

# ismlar
names = np.array(['Hasan' , 'Husan' , 'Mirzabek' , 'Elyor' , 'Hasan' , 'Javohir' , 'Elyor'])
print(names)

# data
data = np.random.randn(7 , 4)
print(data)

# Boolean indekslash - bu massiving elemntlari indeksi True va False lardan iborat bo'ladi

print(names == 'Hasan') # Ismlar massivini boolean indekslash
# Natija
# [ True False False False  True False False]

print(data[names == "Hasan"]) # "Hasan" elemntiga tegishli ma'lumotlarni ajratib olish
print(data[names == 'Elyor']) # "Elyor" elemntiga tegishli ma'lumotlarni ajratib olish
print(data[names == 'Javohir']) # "Javohir" elemntiga tegishli ma'lumotlarni ajratib olish


print(data[names == 'Hasan' , 2: ]) # 'Hasan' elementiga tegishli oxirgi ikkita ustun ma'lumotlarini ajratib olish
print(data[names=="Hasan" ][1 , :2]) # "Hasan" elemntiga tegishli dastlabki 2 ta ma'lumotni kesib olish

print(data[names != 'Hasan']) # (!=)   "Hasan" elemntiga tegishli bo'lmagan barcha elemtlarni ajratib olish

print(data[~(names == 'Hasan')]) # ( [~()] )   "Hasan" elemntiga tegishli bo'lmagan barcha elemtlarni ajratib olish

print((names == 'Hasan') | (names == 'Elyor')) # birdaniga 2 ta elemntni boolean indekslash

print(data[(names == 'Hasan') | (names == 'Elyor')]) # ( | ) or (yoki) degani
data[data<0] = 0 # manfiy sonlarnin nolga tenglash
print(data)
