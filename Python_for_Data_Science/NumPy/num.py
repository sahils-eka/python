import numpy as np

arr = np.array([1, 2, 7, 9])
# # print(arr*2)
# u = np.array([1, 5])
# v = np.array([6, 3])
# z = u + v
# dot = np.dot(u, v)
# # print(z)
# # print("Dot product of u & v : ", dot)
# # print("Max value of array arr: ", np.max(arr))
# # print("Min of array : ", np.min(arr))
# # print("Mean of array arr: ", np.mean(arr))

# print(np.sin(np.pi))
newArr = [0, 3, 2]
arr1 = np.copy(arr)
# arr2 = arr.view()
# print(arr1)
# print(arr1.base)
# print(arr2.base)

# print(arr[newArr])

# arr[newArr] = 22

# print(len(arr), arr.size)

# a = np.array([5, 9, 8, 6, 1])
# print(a.std())

# x = np.array([0, np.pi/2, np.pi])

# y = np.sin(x)

# print(y)


# print(np.linspace(2, 10, num=5))

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(arr2.shape)
# print(arr2.ndim)

# print(arr2[0, 0::2])

A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])

matrix = np.dot(A, B)

print(matrix)
print("Sin of Matrix", np.sin(matrix))

print("Transposed Matrix\n", matrix.T)
