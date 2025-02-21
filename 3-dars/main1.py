import numpy as np #kutubxonani chaqirib olish

# 3-dars . NumPy kutubxonasida indekslash va kesish amallari

#oddiy kesib olish
arr1d = np.arange(1 , 10 , 1 , dtype=np.int8) #1 dan 10 gacha 1 qadam bilan o'sayotgan massivni yaratamiz int8 tipida
print(arr1d) #massivni chiqaramiz

sliced_arr = arr1d[3:5] #massivning 3-dan 5-gacha (5-kirmaydi) elemntlari kesib olindi
sliced_arr[:] = 1 #kesib olingan elementlar ixtiyoriy(1) songa tenglashtirildi

print(sliced_arr)
print(arr1d) # bu yerda kesib olingan elemntlarimizning 1 ga tenglashgani massivga ham ta'sir qiladi



arr_1d = np.arange(1, 10, 1 , dtype=np.int8) #yangi massiv yaratdik
print(arr_1d) #massivni chiqaramiz

# .copy() metodi
sliced_arr_1d = arr_1d[3:5].copy() #bu yerda .copy() metodi bilan massivning biz istagan elemtnlarini kopiya qilib olamiz
sliced_arr_1d[:] = 1 #bu yerda ham kesib olingan elementlar ixtiyoriy(1) songa tenglashtirildi

print(sliced_arr_1d) #sliced_arr_1d chiqarildi
print(arr_1d) #bu method orqali kesib olingan elemntlarimizning 1 ga tenglashgani massivga ham ta'sir qilmaydi


# 2d massivning indekslanishi va kesilishi
data2d = [[1, 2, 3, 4, 5] , [6, 7, 8, 9, 10]] # 2d oddiy list
arr2d = np.array(data2d) # 2d npdarray

sliced_2d = arr2d[1 , 3:].copy() # kesish [qator , dastlabki element ustuni: oxirgi element ustuni (bo'lmasa oxirigacha)]
# sliced_2d[:] = 0
print(sliced_2d)
print(arr2d)


# 3d massivning indekslanishi va kesilishi
data3d = [[[ 0,  1,  2],
                [ 3,  4,  5],
                [ 6,  7,  8]],

               [[ 9, 10, 11],
                [12, 13, 14],   # har bir elemntni indeksi [ (massivi) ] [ (satri) , (ustuni) ] , misol [1][0][2]= 11
                [15, 16, 17]],

               [[18, 19, 20],
                [21, 22, 23],
                [24, 25, 26]]]
arr_3d = np.array(data3d)

print(arr_3d[1][0][2])

sliced_3d = arr_3d[1][1: , :2] # [massivning indeksi][satr boshlanish indeksi : satr tugash indeksi , qator boshlanish indeksi : qator tugash indeksi]
print(sliced_3d)