import numpy as np
import matplotlib.pyplot as plt

# Create a 2D Numpy array of size 1x3 with elements of your choice
arr1=np.array([[1,2,3],])

# Create a Numpy array of length 50 with zeroes as its elements
arr2=np.zeros(50)

#Create a Numpy array of length 3x2 with elements of your choice
arr3=np.array([[1,2],[3,4],[5,6]])

#Multiply arr1 and arr3 using Numpy functions
arr4= np.dot(arr1,arr3)


'''
np.zeros((1 , 2))

for x in range(1):
  for z in range(2):
    for y in range(3):
      arr4[x,z] += arr1[x,y]*arr3[y,z]
      
'''      

#Change 5th element of arr2 to a different number
arr2[4] = 1

if np.shape(arr4)==(1,2) and arr2[4]!=0:
  print("Passed")
else:
  print("Fail")

#--------------------------------------------------------------------#

#dot product of I and 9I+1
arr5 = np.identity(3)
arr6 = 9*np.identity(3)
arr7 = np.dot(arr5,arr6) + np.dot(arr5,1)
print(arr7)

#---------------------------------------------------------------------#

xpoints=np.array([1,2,3,4])
ypoints=np.array([2,4,6,8])

#Plot these points without drawing a line
#plt.plot(xpoints,ypoints,'o')

#Plotting with marker: Plot these points with a marker(Star marker)
#plt.plot(xpoints,ypoints,'*')

#Using fmt format, add circular marker,red color and Dashed line
#plt.plot(xpoints,ypoints,'o--r')

#Add xlabel,ylabel and title for the plot.
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")

#Create a scatter plot for xpoints and ypoints
#plt.scatter(xpoints,ypoints)

#Set color to the scatter plot. Blue,Green,Red and yellow color for each point respectively
colours = np.array(("blue","green","red","yellow"))
#plt.scatter(xpoints,ypoints, c=colours)
#plt.show()

#-------------------------------------#

#Set the seed of random to 20
#Your code here
np.random.seed(20)

arr10=np.array([1,24,31,45,73,81,94,25])

#Using the random module pick 4 different random numbers from arr10 and return their sum.
#Your code here
arr11=np.random.choice(arr10, size=(4))
global sum
sum = [0,]
def fourSum(arr,sum ,k):
  x = np.random.choice(arr)
  print(x)
  print(arr)
  ind = np.where(arr==x)
  sum[0] += x
  if(k!=1):
    fourSum(np.delete(arr,ind),sum,k-1)

fourSum(arr10,sum,4)
print(sum[0])

