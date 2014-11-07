from pandas import *
from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
randn=np.random.randn
path='/Users/Yann/Desktop/Python/DB/Bikes.csv'
import pandas as pd

s = Series(randn(5), index=['a', 'b', 'c', 'd', 'e'])
print("s= " )
print(s)


print("Series(randn(5))")
s=Series(randn(5),index=['a', 'b', 'c', 'd', 'e'])
print("s= " )
print(s)

d = {'a' : 0., 'b' : 1., 'c' : 2.}
#print(Series(d))
#print(Series(5.,index=['a','b','c']))
#print("s[0] = ",s[0])
#print(s[1:3])
#print(s[s>s.median()])
#print(s[[1,3,2]])
#print(np.exp(s))
#print(s['a'],s['d'],s[3])
#print('a' in s)

#dataframes

d = {'one' : Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df=DataFrame(d)
print(df)

data = np.zeros((2,),dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
data[:] = [(1,2.,'Hello'),(2,3.,"World")]

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(DataFrame(data2))

#import de Yahoo

import pandas.io.data as web
import datetime
start=datetime.datetime(2014,1,1)
end=datetime.datetime(2014,9,29)

AAPL=web.DataReader("AAPL",'yahoo',start,end)
print(AAPL)
matrix=AAPL.values
print(matrix)
print(matrix[2][2])

