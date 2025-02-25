# Chiziqli algebra amallari

import numpy as np # kutubxonani chaqirib olish


from numpy.linalg import inv # chiziqli algebra modulidan inversiya ni chqirib olish



x = np.array([[1. , 2. , 3.] , [4. , 5. , 6.]]) # x matritsa
print(x)

y = np.array([[5. , 5. , 5.] , [4. , 4. , 4.]])
print(y)

# matritsalarni qo'shish va ayrish
data1 = x + y # matritsa elemntlarini bir-biriga qo'shamiz
print(data1)

data2 = y - x # matritsa elemntlarini bir-biriga ayiramiz
print(data2)

# skalyar ko'paytirish (matritsa har bir elementini aynan bir songa ko'paytirish)
data3 = x * 5
print(data3)



# Matritsalar aro ko'paytirish
# Ikki matritsani ko'paytirish uchun 1-matritsa qatorlar soni 2-matritsa ustunlari soniga teng bo'lishi kerak

a = np.array([[1. , 2. , 3.] , [4. , 5. , 6.]])
b = np.array([[6. , 23.] , [-1 , 7] , [8 , 9]])

c = a.dot(b) # a matritsa ko'paytirilgan b matritsa ( np.dot(a , b) )
d = b.dot(a)
print(c)
print(d)

# Linear Algebra
from numpy.linalg import inv # chiziqli algebra modulidan inversiya ni chqirib olish


