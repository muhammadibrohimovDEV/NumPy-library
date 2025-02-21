import numpy as np #kutubxonani chaqirib olish

# 5-dars . NumPy kutubxonasida massiv o'qlarini almashtirish

# Transpoze - massiv elemtnlarini shaklini o'zgartirish , misol (3 , 2) -> (2 , 3)
# Sodda qilib aytadigan bo'lsak , matritsa transpaneli
# Lekin maximum 2 -o'lxhamli massivlargacha almashtira olamiz

arr = np.arange(0 , 6 , 1)
arr = arr.reshape(3,2)
print(arr.T)  # transpanellash .T


# swapping axes . - Tranpoze bilan bir xil

print(arr)

arr1 = arr.swapaxes(1 , 0) # Transpoze bilan bir xil

print(arr1)

# A*A.T


# .dor - ko'paytirish funksiyasi

data = np.dot(arr , arr1) # arr va arr.T hosil bo'lgan massiv
print(data)