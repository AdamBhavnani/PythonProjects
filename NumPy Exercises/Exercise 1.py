import numpy as np

## Exercise 1
#print(np.__version__)
#print(np.show_config())

## Exercise 2
#print(np.info(np.add))

## Exercise 3
#x = np.array([1,2,3,4,0,8])
#a = np.all(x)
#print(a)

## Exercise 4
#x = np.array([1,2,3,4,0,8])
#a = np.any(x)
#print(a)

## Exercise 5
#a = np.array([0,1,2,np.nan,np.inf])
#print(np.isfinite(a))

## Exercise 6
#a = np.array([-np.inf,np.inf])
#print(np.isneginf(a))

## Exercise 7
#a = np.array([0,1,np.nan])
#print(np.isnan(a))

## Exercise 8
#a = np.array([0,1,1+1j,4,2j,3.5])
#print(np.iscomplex(a))
#print(np.isreal(a))
#print(np.isscalar(3.1))

## Exercise 9
#a = np.array([1,2,4.56789])
#b = np.array([1,2,4.56789])
#c = np.array([1,2,4.5678])
#print(np.allclose(a,b,1.e-5))
#print(np.allclose(b,c,1.e-5))

## Exercise 10
#a = np.array([3,5])
#b = np.array([1,5])
#print(np.greater(a,b))
#print(np.greater_equal(a,b))
#print(np.less(a,b))
#print(np.less_equal(a,b))

## Exercise 11
#a = np.array([1,5,100.111])
#b = np.array([1,5,100.11])
#print(np.greater(a,b))
#print(np.greater_equal(a,b))

## Exercise 12
#a = np.array([1,7,13,105])
#print(a.size)
#print(a.itemsize)
#print("%d bytes" % (a.size * a.itemsize))

## Exercise 13
#a = np.zeros(10)
#a = np.ones(10)
#a = np.ones(10)*5

## Exercise 14
#a = np.arange(30,71,1)
#print(a)

## Exercise 15
#a = np.arange(30,71,2)
#print(a)

## Exercise 16
#a = np.identity(3,int)
#print(a)

## Exercise 17
#print(np.random.normal(0,1,1))

## Exercise 18
#print(np.random.normal(0,1,15))

## Exercise 19
#a = np.arange(15,56)
#print(a)
#print(a[1:-1])#print second element to second last 

## Exercise 20
#a = np.arange(10,22)#vector from 10 to 22
#print(a)
#a = np.arange(10,22).reshape((3,4))#sequentially place elements into 3x4 matrix
#print(a)
#for x in np.nditer(a):
#    print(x)

## Exercise 21 
#a = np.linspace(5,50,10)
#print(a)
#print(len(a))

