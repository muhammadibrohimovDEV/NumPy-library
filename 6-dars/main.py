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
# Eksponential funksiyani bajaradi (e darajsi element).
print(data3)

# log
data4 = np.log(arr) # .log() massivning har bir elemntini logarifmini (log e) qaytaradi
print(data4)

data10 = np.log10(arr) # .logarifm 10 asosga ko'ra massivning elemnti
data10 = np.log2(arr) # .logarifm 2 asosga ko'ra massivning elemnti
data10 = np.log1p(arr) # .logarifm 1+x asosga ko'ra massivning elemnti



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



# abs , fabs
print()
arr_0 = np.array([-10 , -12 , 20 , 0.5])
print(arr_0)
print(np.abs(arr_0)) # har bir elemntning maximum qiymatini qaytaradi
print(np.fabs(arr_0))
print()

# ceil
yaxlitla = np.array([1.2 , 2.5 , 3.6 , -6.3]) # .ceil() o'zidan 1 katta songa yaxlitlaydi
print(yaxlitla)
print(np.ceil(yaxlitla))

# floor
print(yaxlitla)
print(np.floor(yaxlitla)) # .floor() o'zidan 1 kichik songa yaxlitlaydi


# rint
print(yaxlitla)
print(np.rint(yaxlitla)) # .rint() o'ziga eng yaqin butun songa yaxlitlaydi







# Binary funksiyalar - ikkita argument qabul qiluvchi funksiyalar

# add
arr2 = np.random.randn(6)
arr3 = np.random.randn(6)

print(arr2 , '\n' , arr3)

data9 = np.add(arr2 , arr3) # .add() ikki massivning mos elemntlarinining yig'indisini qaytaradi
print(data9)

# substarkt
print(arr2 , '\n' , arr3)

data11 = np.add(arr2 , arr3) # .add() ikki massivning mos elemntlarinining ayrimasini qaytaradi
print(data11)


# multiply
data12 = np.multiply(arr2 , arr3) # 2 massivlarning mos indeksadagi elemntlarini bir-biriga ko'paytiradi
print(data12)


# maximum , minimum
data13 = np.maximum(arr2 , arr3) # 2 massiv mos indeksdagi elemntlarini taqqoslaydi va kattalarini massiv ko'rinishida qaytaradi
print(data13)
data13 = np.minimum(arr2 , arr3) # 2 massiv mos indeksdagi elemntlarini taqqoslaydi va kichiklarini massiv ko'rinishida qaytaradi
print(data13)

# fmax , fmin
print(np.fmax(arr2 , arr3)) # 2 massiv mos indeksdagi elemntlarini taqqoslaydi va kattalarini massiv ko'rinishida qaytaradi faqat Nan elementlarni hispbga olmaydi
print(np.fmin(arr2 , arr3)) # 2 massiv mos indeksdagi elemntlarini taqqoslaydi va kichiklarini massiv ko'rinishida qaytaradi faqat Nan elementlarni hispbga olmaydi

# power
arr_14 = np.array([2 , 3 , 4])
arr_141 = np.array([3 , 4 , 5])
data_14 = np.power(arr_14 , arr_141) # birinchi massivning mos indeksdagi elemntlarini ikkinchi massivning mos indeksdagi elemntlarining dajatraiga ko'tradi
print(data_14)

# mod
# Mos indekslardagi elemntlarni bo'lib faqat butun qismini qaytaradi
x = np.array([10, 20, 30])
y = np.array([3, 7, 4])
print(np.mod(x, y))       # [1 6 2] → 10%3=1, 20%7=6, 30%4=2


# copysign
# Ikkinchi massivdagi mos elemnt ishorasini birichisiga ko'chiradi
a = np.array([1, -2, 3])
b = np.array([-1, 1, -1])
print(np.copysign(a, b))  # [-1.  2. -3.] → Ishtiroklar ikkinchi arrayga moslashtiriladi

