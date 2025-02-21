# 6-dars . NumPy ktubxonasida qo'llaniladigan universal funksiyalar

import numpy as np # kutubxonani chaqirib olsih

# 1-guruh funksiyalar .  Unary funksiyalar (bitta argument qabul qiluvchi)

arr = np.arange(1 , 11) # array yaratib oldik

# sqtr
data1 = np.sqrt(arr) # .sqrt() fiunksiyasi massivning barcha elemntlaridan kvadrat ildiz qaytaradi
print(data1)

# square
data2 = np.square(arr) # .square() funksiyasi massivning har bir elemntini kvadratga oshiradi
print(data2)

# exp
data3 = np.exp(arr) # .exp() massiv elemntlarining barchasini eksponentasini qaytaradi
print(data3)

# log
data4 = np.log(arr) # .log() massivning har bir elemntini logarifmini (log e) qaytaradi
print(data4)

# modf
arr1 = np.random.randn(6)
print(arr1)
data5 , data6 = np.modf(arr1) # .modf() haqiqiy sonlardan iborat massiv elemntlarining butun qismini bir massivga qoldiq qismini boshqa massivga ajratib beradi
print(data5 , "\n" , data6)

# sign
data7 = np.sign(arr1)  # .sign() agar massivning elemnti manfiy bo'lsa -1 , musbat bo'lsa 1 qaytaradi
print(data7)

# isnan
arr1[3] = np.nan # ixtiyoriy indeksdagi elemntni NaN qiymatga almashtirish
print(arr1)

data8 = np.isnan(arr1)  # massivning elemnti agar NaN bo'lsa True , bo'lamasa False qaytaradi
print(data8)



# Binary funksiyalar - ikkita argument qabul qiluvchi funksiyalar

# add
arr2 = np.random.randn(6)
arr3 = np.random.randn(6)

print(arr2 , '\n' , arr3)

data9 = np.add(arr2 , arr3) # .add() ikki massivning mos elemntlarinining yig'indisini qaytaradi
print(data9)


# multiply
data10 = np.multiply(arr2 , arr3) # 2 massivlarning mos indeksadagi elemntlarini bir-biriga ko'paytiradi
print(data10)


# maximum
data11 = np.maximum(arr2 , arr3) # 2 massiv mos indeksdagi elemntlarini taqqoslaydi va kattalarini massiv ko'rinishida qaytaradi
print(data11)

