import numpy as np
simple_array = np.arange(10) #range function in numpy
print("Print using numpy arange ", simple_array)
float_array = np.arange(10, dtype=float) #possible to change data type
print("Conver array to float type ", float_array)
complex_array = float_array.astype(complex)
print("Comples convert ", complex_array)
int_list = [1,67,83,90,12,234,561,78,9,11]
int_list = np.array(int_list) #array from list
print ("Convert list to array ", int_list)
scores_array = np.genfromtxt('scores.csv', delimiter = ',', dtype=int) #array from csv
print("Content from CSV file to array ", scores_array)
print("Slicing an array ", scores_array[0: 2]) #slicing


'''
Reshaping a Numpy Array into a matrix'''
a = np.array([1,2,3,5,6,6,7,8,1,3])
print("Shape of array or matrix ", a.shape) #a is a list here not matrix
matrix = a.reshape(2,5) #reshaped the array into matrix
print("Reshape list to matrix ",  matrix)

A = np.array([1,2,3])
print ("Array A ", A)
B = np.array([4,5,6])
print ("Array B ", B)
C = np.vstack((A, B)) #vertical stack
print ("Vertical stack A on B \n", C)
D = np.hstack((A,B)) #horizontal stack
print("Horizontal stack B next to A ", D)
'''PS: All the input arrays to be stacked must be of the same dimension'''
A1 = np.array([[1,2,3], [4,5,6]])
B1 = np.array([[7,8,9], [10,11,12]])
C1 = np.concatenate((A1,B1), axis = None)
print ("concatenate axis = None \n", C1)
D1 = np.concatenate((A1,B1), axis = 0)
print ("concatenate using axis = 0 i.e. horizontally\n", D1)
E1 = np.concatenate((A1,B1), axis = 1)
print ("Concatenate using axis=1 i.e. vertically\n", E1)

#Revenue = Sales @ Price to calculate two matrices multiplication
