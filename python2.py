#Aggregation functions of array
import numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])
print("Sum of the array = ",a.sum())
print("Maximum of the array = ",a.max())
print("Minimum of the array = ",a.min())
print("Maximum of the array = ",a.max(axis=1))
print("Minimum of the array = ",a.min(axis=1))
print("Cumilative Sum of the array = ",a.cumsum(axis=1))
print("Cumilative Sum of the array = ",a.cumsum())
print("Average of the array = ",a.mean())
print("transpose of an array: ",a.transpose())
print("sum of two arrays:",a+b)
