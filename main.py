# N-dimensional Array (NumPy)

# kutubxonani chaqirish
import numpy as np

data = [1, 2, 3, 4, 5] # python list
arr = np.array(data)
print(arr)
print(type(arr))  # <class 'numpy.ndarray'>


# 2D massiv (matritsa)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# 3D massiv
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d)



arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)  # O'lcham soni (2D massiv - 2)
print(arr.shape)  # O'lcham o'lchovlari (qator, ustun)
print(arr.size)   # Elementlar soni
print(arr.dtype)  # Ma’lumot turi



print(np.zeros((3, 4)))   # 3x4 nol massivi
print(np.ones((2, 5)))    # 2x5 birlik massivi
print(np.full((2, 3), 7)) # 2x3 butun 7 bilan to‘ldirilgan massiv
print(np.eye(4))          # 4x4 birlik matritsa


print(np.random.rand(3, 3))     # 3x3 massiv (0-1 oralig‘ida)
print(np.random.randint(1, 10, (2, 3)))  # 2x3 butun sonlar massivi
print(np.random.randn(3, 3))    # Normallangan taqsimotga ega massiv



arr = np.array([10, 20, 30, 40, 50])
print(arr[0])  # 10
print(arr[-1]) # 50


print(arr[1:4])   # [20 30 40]
print(arr[:3])    # [10 20 30]
print(arr[::2])   # [10 30 50]  (har ikkinchi element)


arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 2])  # 6 (2-qator, 3-ustun)
print(arr_2d[:, 1])  # [2 5 8] (2-ustun)


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # [5 7 9]
print(arr1 * arr2)  # [4 10 18]
print(arr1 ** 2)    # [1 4 9]
print(np.sqrt(arr1)) # [1. 1.414 1.732]
print(np.exp(arr1))  # e^x
print(np.sin(arr1))  # sinus


arr = np.array([1, 2, 3, 4, 5])

print(np.mean(arr))   # O‘rtacha qiymat
print(np.median(arr)) # Median
print(np.std(arr))    # Standart og‘ish
print(np.var(arr))    # Variatsiya
print(np.min(arr))    # Eng kichik qiymat
print(np.max(arr))    # Eng katta qiymat


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))      # Matritsa ko‘paytmasi
print(np.linalg.inv(A))  # A matritsasining teskari matritsasi
print(np.linalg.det(A))  # Determinant
print(np.transpose(A))   # Transpozitsiya

