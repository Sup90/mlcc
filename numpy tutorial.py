# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:42:34 2019

@author: COM
"""

#%%
import pandas as pd
import numpy as np
import sys
import pprint as pp
sys.version
#%%
np.__version__
#%%
pp.pprint("numpy version {}".format(np.__version__))
#%%
x=[1,2,3]
x1=[1,"a",3]
#다른 랭귀지의 어래이가 파이썬의 list라고 보면됨...?
#%%

#튜플은 내용물을 수정할 수 없다.
#리스트는 내용물을 수정 가능

A=np.ones((5,5))
A[0,1:5]
A[:,0]=3 #전체 행에서 0번째 열을 3으로 수정
A=np.zeros((4,5,3))
A[:,:,0]=3
A[2,3,2]=7
print(A)
#%%

B=np.ones((3,3,3))
B[:,0,:]=5
B
#%%
a=np.array([[1,0],[0,1]])
b=np.array([1,2])
a+b #브로드캐스팅을 통해 알아서 행렬 차원을 맞춰서 연사 수행
#element-wise addition
#element-wise multipli
#%%
#같은 결과
print(np.matmul(a,b))
print(a@b)
a.dot(b)
#%%
np.arange(9)
A=np.arange(9).reshape((3,3))
A.transpose()
A.T
B=np.arange(10)
C=B.reshape((2,5))
C.shape
A=np.arange(10).reshape((2,5))
B=np.arange(10).reshape((5,2))
C=np.c_[A,B.T]
np.column_stack([A,B.T])
np.hstack([A,B.reshape(2,5)])
#Transpose(row와 column을 변경)랑 reshape랑은 결과가 다를 수 있다. 
#%%
A.ravel()
A
#%%
np.random.random_sample((3,2))
np.random.rand(3,2) #최화할때(신경망 초기화) 초기값을 정규분포로 주면 값이 잘맞아서
#샘플 데이터를 만들더라도 정규분포 기반으로 씀
