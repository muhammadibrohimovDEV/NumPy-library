import numpy as np # calling the library

list1 = [x for x in range(10)] # list(range(10)) , print(*(for x in range(10))

arr1 = np.array(list1) # array method
print(arr1)

arr2 = np.arange(15) # arange method
arr2 = arr2.reshape(3 , 5) # reshape method
print(arr2)

arr3 = np.zeros((5 , 6) , dtype = np.int8) # zeros method
print(arr3)

arr4 = np.ones((12 , 20) , dtype = np.float16) # zeros method
print(arr4)

arr5 = np.full((2 , 3) , 25) # full method
print(arr5)

arr6 = np.eye(16) # eye method
print(arr6)

arr7 = np.random.rand(5 , 2) # random.rand method
print(arr7)

arr8 = np.random.randint(2 , 20 , (2 , 3)) # random.randint method
print(arr8)

arr9 = np.random.randn(2 , 2) # random.randn method
print(arr9)


