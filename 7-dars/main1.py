# 7-dars . Mantiqiy shart operatorlari

import numpy as np # kutubxonani chqirib olish


# 1-masala . Yangi massiv yaratiladi . Agar True kesa -> xarr , False kelsa -> yarr
# Massivlar

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5]) # xarr
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5]) # yarr

# Shart
cond = np.array([True,False, True , True, False])

# where function
result = np.where(cond , xarr , yarr) # Agar True kesa xarr dan oladi , False kesa yarr dan oladi

print(result)

# 2-masala
arr = np.random.randn(4 , 4) # ictiyoriy (4 , 4) massiv

# where
results = np.where(arr<0 , -2 , 2)
print(results)


# where(condition , (if , else))