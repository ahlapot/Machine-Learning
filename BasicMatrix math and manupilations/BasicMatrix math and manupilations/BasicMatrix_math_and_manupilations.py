import numpy as np

# basic matrix math and manupilations with numpy...

a=np.array([[13,7,14],
           [47,2,9],
           [17,26,5]])

b=np.array([[3,5,7,],
           [2,4,6],
           [0,32,12]])

c=np.array([[5,20,4],
           [7,15,-3],
           [2,11,0]])


# addition 
print('a+b:')
print(a + b)

# substract
print('a-b:')
print(a-b)

# multiply
print('a*b:')
print(a*b)

# divide
print('a/b:')
print(a/b)

# multiplying A by scalar 3
print('A multiplied by scalar 3:')
print(3*a)

# dimensions of each matrix
print('Each matrix has a dimension of 3X3')

# determine the determinant
detc=np.linalg.det(c)
print('Determinant of c')
print(detc)

# resultant transpose of c
print('Resultant transpose of c:')
print(c.transpose())

# resultant inverse of c
invc = np.linalg.inv(c)
print('Resultant inverse of c:')
print(invc)