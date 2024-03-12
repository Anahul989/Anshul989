# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QPO3hR4ceJPGnX-dWv8VK5SUPxtUOw5e
"""

import pandas as pd

import numpy as np

info=np.array(['P','a','n','d','a','s'])

a=pd.Series(info)

print(a)

import pandas as pd
# a list of strings

x = ['Python','Pandas']
#Calling DataFrame constructor on list

df = pd.DataFrame(x)

print(df)

a = pd.Series(['Java','C','C++',np.nan])

a.map({'Java':'Core'})

a=pd.Series(['Java','C','C++',np.nan])

a.map({'Java':'Core'})

a.map('I like{}'.format, na_action='ignore')

s=pd.Series(["a","b","c"],name="vals")

s.to_frame()

#Exersize 2
df=pd.DataFrame()
print(df)

#a list of strings
x=['Python','Pandas']

#Calling DataFrame constructor on list
df=pd.DataFrame(x)

print(df)

info={'ID':[101,102,103],'Department':['B.Sc','B.Tech','M.Tech']}

df=pd.DataFrame(info)

print(df)

info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}

d1=pd.DataFrame(info)

print(d1)

info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}

d1=pd.DataFrame(info)

print(d1['one'])

import pandas as pd
info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
d1=pd.DataFrame(info)

df=pd.DataFrame(info)

print("Add new column by passing series")

df['three']=pd.Series([20,40,60],index=['a','b','c'])
print(df)

print("Add new column using existing DataFrame column")

df['four']=df['one']+df['three']
print(df)

import pandas as pd

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(info)
print("The DataFrame")
print(df)
#using del funtion
print("Delete the first column")
del df['one']
print(df)
#using pop function
print("Delete the another column ")
df.pop("two")
print(df)

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(info)
print(df.loc['b'])

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
d1=pd.DataFrame(info)
print(df.iloc[3])

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
d1=pd.DataFrame(info)
print(df[2:5])

d=pd.DataFrame([[7,8],[9,10]],columns=['x','y'])
d2=pd.DataFrame([[11,12],[13,14]],columns=['x','y'])
d=d.append(d2)
print(d)

a_info=pd.DataFrame([[4,5],[6,7]],columns=['x','y'])
b_info=pd.DataFrame([[8,9],[10,11]],columns=['x','y'])
a_info=a_info.append(b_info)
a_info=a_info.drop(0)

#Exersise 07
dict={'name':["Smith","William","Phill","Parker"],'age':["28","39","34","36"]}
info=pd.DataFrame(dict,index=[True,True,False,True])
print(info)

dict={'name':["Smith","William","Phill","Parker"],'age':["28","39","34","36"]}
info=pd.DataFrame(dict,index=[True,True,False,True])
print(info.loc[True])

import numpy as np
arr=np.arange(16)
print("The Original array is:\n",arr)
arr=np.arange(16).reshape(2,8)
print("\nreshapedarray:\n",arr)
arr=np.arange(16).reshape(8,2)
print("\nreshaped array:\n",arr)

#exercise 8
a=np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,0],b[0,1],b[1,0])

import numpy as np
a=np.zeros((2,2))
print(a)

b=np.ones((1,2))
print(b)

c=np.full((2,2),8)
print(c)

d=np.eye(2)
print(d)

e=np.random.random((2,2))

print(e)

