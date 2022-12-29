import numpy as np

# lists working

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

print(list_a * list_b)

import numpy as np
numpy_a = np.array([1,2,3,4])
numpy_b = np.array([5,6,7,8])

print(numpy_a)

print(numpy_a * numpy_b)

# common properties

numpyBasic_array = np.array([1,2,3,4, 5, 10.5, "a"])

print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)

print((numpyBasic_array.size))




# 2d Arrays

array_1D = np.array(([[[1,2,3], [3,4,5]], [[1,2,3], [3,4,5]] ]))
array_2D = np.array([[1,2,3], [3,4,5], [6,7,8]])

print(array_2D)
print("Dimensions: {}".format(array_2D.ndim))
print("Shape: {}".format(array_2D.shape))
print("Array Dtype: {}".format(array_2D.dtype))

array_2D = np.array([1,2,3],dtype='float64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)


# accessing arrays
array_x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print(array_x)
print(array_x.size)

print(array_x[1,2])
print(array_x[0,2])
print(array_x[:, 2])
print(array_x[: , -3])

# step - start :end: stepsize
print(array_x[0, 0: 4: 2])

print(array_x[:, 0: 4: 2])

array_x[0,2] = 10


array_x[:,2] = 10

# 3d arrays

array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array_3d)

print(array_3d[0,1,0])

print(array_3d[:, 1, 1])

print(array_3d[:,:,0])

#3d array updation

array_3d[:, 0, :] = 100
print(array_3d)


array_3d = np.array([[[1,2],[3,4]], [[1,2,7],[3,4,8]]])
print(array_3d)
print(array_3d.shape)



array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array_3d)

print(array_3d[:, 0, :])

array_3d[:, 0, :] = [[10,10], [20,20]]
print(array_3d)


# common arrays
#one's two's empty

print(np.zeros(3))

print(np.ones(3))

two_d = np.zeros((3,3))
print(two_d)


three_d = np.zeros((2,3,3))
print(three_d)

four_d = np.zeros((2,3,3,2),dtype="int32")

print(four_d)

print(np.zeros((3,3)))

print(np.full((3,3),[1,2,3]))

print(np.full((3,3),[1,2,3],dtype="float32"))


array_a = [1,2,3]
print(np.full_like(array_a, 4))

# repeat

array_r = [[1,2,3], [4,5,6]]


array_repeat = np.repeat(array_r,2, axis=1)

print(array_repeat)

array_zeros = np.zeros((3,3))

array_zeros[1,1] = 7

print(array_zeros)

updated_array = np.zeros((5,5))
updated_array[1:-1, 1:-1] = array_zeros

print(updated_array)


# copying arrays

array_x = np.array([1,2,3,4])

array_y = array_x

array_y[0] = 7

print(array_x)
print(array_y)



array_x = np.array([3,5,6,7])

array_y = array_x.copy()

array_y[0] = 10

print(array_x)
print(array_y)


# math operations

array_math = np.array([1,2,3])

print(np.sin)

print("Declared array: {}".format(array_math))
print("Add 10 to  array: {}".format(array_math + 10))
print("sub to from array: {}".format(array_math - 10))
print("raise to pow array: {}".format(array_math ** 2))
print("mul array by 5: {}".format(array_math * 5))
print("div array by 2: {}".format(array_math / 2))


# Algerba with numpy


arr_a = np.ones((2,3))

arr_b = np.full((3,2), 2)

print(arr_b)
print(arr_a)


print(arr_a * arr_b)

print(np.matmul(arr_b, arr_a))

# statistics

n_a = [[1,1,1,1], [0,0,0,0,0,0,0]]
print(n_a)


array_stats = [[1,2,3], [4,5,-6]]

print(np.min(array_stats))
print(np.min(array_stats, axis= 1))

print(np.max(array_stats))
print(np.max(array_stats, axis= 1))

print(np.sum(array_stats, axis=1))


# reshape

array_stats =np.array( [[1,2,3,7], [4,5,-6,4]])

print(array_stats.reshape((4,2)))

# stacking

a_v1 = np.array([1,2,3,4])

a_v2 = np.array([1,2,3,4])

print(np.array([a_v1, a_v2]))


print(np.hstack([a_v1, a_v2]))