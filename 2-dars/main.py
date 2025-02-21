import numpy as np # kutubxonani chaqirib olish
# 2-dars . NumPy kutubxonasida ma'lumot turlari

# bool - True or False 1 bayt
# intc - C dasturlash tilidagi ma'lumot turi bilan bir xil (int32 , int64)
# int8 - 8 baytlik butun sonlar (-128 , 128)
# int16 - 16 baytlik butun sonlar (-32768 , 32767)
# int32 - 32 baytlik butun sonlar (-2147483648 , 2147483647)
# int64 - 64 baytlik butun sonlar (-9223372036854775808 , 9223372036854775807)
# uint8 - musbat int8 (0 , 255)
# uint16 - musbat int16 (0 , 65535)
# uint32 - musbat int32 (0 , 4294967295)
# uint64 - musbat int64 (0 , 18446744073709551615)
# float16 - butun bo'lmagan qismiga ega sonlar (5 butun qiymat , 10 butun emas)
# float32 - butun bo'lmagan qismiga ega sonlar (8 butun qiymat , 23 butun emas)
# float64 - butun bo'lmagan qismiga ega sonlar (11 butun qiymat , 52 butun emas)
# complex64 - 2ta 32 bitlik float sondan iborat  
# complex128 - 2ta 64 bitlik float sondan iborat
# string - ASCII string turi (1 baytdan) 

# dtype metodi
arr = np.arange(1 , 20 , 2)
arr.dtype = np.int8 # dtype metodi massivning ma'lumot turini ko'rsatadi va uning turini almashtira oladi
print(arr.dtype)

# shape metodi
arr1 = np.array([[1,2,3,4,5] , [6,7,8,9,10]])
arr1.shape = (5,2) # shaklini o'zgartirsa boladi
print(arr1)
print(arr1.shape) # (qarot va ustunlar soni)

# size metodi
arr_1 = np.arange(1 , 10 , 1)
print(arr_1)
print(arr_1.size) # size metodi massivda jami nechta elemntlar borligini bildiradi

# ndim metodi
arr__1 = np.arange(1 , 20 , 2 , dtype = np.int8)
print(arr__1.ndim) # ndim metodi nechi o'lchamli ekanini ko'rsatadi

#astype mtodi
arr___1 = np.array([1, 2, 3, 4])
print(arr___1.dtype)
arr___1 = arr___1.astype(np.float64) # massiv elementlari turlarini o'zgartiradi
print(arr___1.dtype)

