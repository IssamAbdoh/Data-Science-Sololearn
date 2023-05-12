import numpy as np

def printStarz():
    print("")
    print("*" * 50)
    print("")

#####################################################################################################################

"""
Performing mathematical operations on arrays is straightforward. For instance, 
to convert the heights from centimeters to feet, 
knowing that 1 centimeter is equal to 0.0328084 feet, 
we can use multiplication:

Now we have all heights in feet. Note that this operation won’t change the original array, 
it returns a new 1darray where 0.0328084 has been multiplied to each element in the first column of 'heights_age_arr'.
"""

heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))

heights_arr = heights_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))

print(height_age_arr[:,0]*0.0328084)
printStarz()

########################################################################

"""
the sum() method finds the sum of all the elements in an array
"""

print(height_age_arr.sum())
printStarz()

########################################################################

"""
In order to sum all heights and sum all ages separately, 
we can specify axis=0 to calculate the sum across the rows, 
that is, it computes the sum for each column, or column sum. 
On the other hand, to obtain the row sums specify axis=1. 
In this example, we want to calculate the total sum of heights and ages, respectively :
"""

print(height_age_arr.sum(axis=0))
printStarz()

#Other operations, such as .min(), .max(), .mean(), work in a similar way to .sum().

########################################################################

print(height_age_arr)
print(height_age_arr[:, 1] )
print(height_age_arr[:, 1] < 55)
print((height_age_arr[:, 1] < 55).sum())
printStarz()

#True is treated as 1 and False as 0 in the sum.

########################################################################

mask = height_age_arr[:, 0] >= 182
tall_presidents = height_age_arr[mask, ]
tall_presidents.shape

print(tall_presidents.shape)
printStarz()

"""
Masking is used to extract, modify, count, or otherwise manipulate values in an array based on some criterion. 
In our example, the criteria was height of 182cm or taller.
"""

########################################################################

#We can create a mask satisfying more than one criteria.

mask = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)

print(height_age_arr[mask,])
printStarz()

########################################################################

print(np.array([1,2,3]).shape)
printStarz()

print(np.array([[1,2,3],[1,2,3]]).shape)
printStarz()

########################################################################


