# Fayllar bilan ishlash
# Asosan ikki sanoq sistemasidagi fayllar bilan ishlanadi ( Binaryu files )

import numpy as np # kutubxonani chaqirib olish

# data
arr = np.arange(10)
print(arr)

# save metodi
# numpy fayllar .npy bilan tugaydi

np.save('data.npy' , arr ) # save faqat bir dona massiv uchun ishlaydi
arr2 = np.load('data.npy')

print(arr2)

# savez metodi
# numpy fayllar .npy bilan tugaydi
arr2d = np.random.randn(2 , 3)
arr3d = np.random.randn(2 , 3 , 2)
print(arr2d)
print(arr3d)
np.savez('arrays.npz' , a = arr2d , b = arr3d) # ikki va undan ortiq massivlar uchun

arrs = np.load("arrays.npz")
print(arrs["a"])
print(arrs["b"])


# savez_compressed - fayllar kamroq xotiradan joy oladi , siqiladi
np.savez_compressed('arrays_compressed.npz' , a = arr2d , b = arr3d)




