# 1-dars . NumPy kutubxonasida array yaratish usullari

import numpy as np #kutubxonani chaqirib oldik

# N-Dimensional Array (npdarray) yaratish usullari  (N-o'lchamli massiv)

#1-metod .array() metodi
data = [1, 2, 3, 4, 5] #oddiy list yaratib oldik
arr = np.array(data) #.array() metodi bilan yaratgan listimizni 'n-dimensional array (npdarray)' ga o'girib oldik

print(arr) # arrayimizni chiqaramiz
print(type(arr)) # haqiqatdan ndarray ekaniga ishonch hosil qilamiz


#2-metod .arange() metodi
arr1 = np.arange(1 , 10 , 2 , dtype = np.int8) #.arange( start , stop(not including 'stop') , step , dtype = np.(type))
print(arr1) # massivimizni chiqaramiz
print(type(arr1)) # haqiqatdan ndarray ekaniga ishonch hosil qilamiz


#3-metod  .zeros() metodi
arr0 = np.zeros((2 , 3) , dtype = np.int8 , order="C") # .zeros( shape() , dtype = np.(type) , order = "C" ("F") ) . Faqat noldan(0) iborat massiv
print(arr0) # massivni chiqaramiz
print(type(arr0)) # haqiqatdan ndarray ekaniga ishonch hosil qilamiz


#3-metod .ones() metodi
arr_1 = np.ones((3,2) , dtype = np.float16 , order = "C") # .ones( shape() , dtype = np.(type) , order = "C" ("F") ) . Faqat birdan(1) iborat massiv
print(arr_1) # massivni chiqaramiz
print(type(arr_1)) # haqiqatdan ndarray ekaniga ishonch hosil qilamiz


#4-metod .full() metodi
arr_full = np.full((2,7),13) # .full(shape(x,y) , fill_value , dtype = np.(type))
print(arr_full)

#5-metod .eye() metodi
arr_eye = np.eye(4) # eye(n (shape(n,n)) , dtype = np.(type)) , birlik matritsa qaytaradi
print(arr_eye)

#6-metod .random metodlari

#.random.rand() metodi
arr_rand = np.random.rand(5 , 2 , 3) # .random.rand(shape (massiv soni , qator soni , ustun soni)) , 0 va 1 oralig'idagi ixtiyoriy son
print(arr_rand)

#.random.randint() metodi
arr_randint = np.random.randint(5 , 15 , size=(5 , 2 , 3) , dtype = np.int8)#.random.randint(low, high=None, size=(massiv soni , qator soni , ustun soni), dtype=np.(type))
print(arr_randint)


#.random.randn() metodi
arr_randn = np.random.randn(5 , 2 , 2) # -1 dan 1 gacha ixtiyoriy son qayataradi
print(arr_randn)
