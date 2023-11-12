import numpy as np

k = [[2, 3, 4], [5, 6, 7]]
print(np.reshape (k, 6)) # reshape : 특정 n by m 행렬 -> 1 by n*m 행렬로 변환
# 인공신경망의 input layer는 1차원 배열로 대입

p = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print (p) # matrix 형태로 출력
print (np.ndim(p)) # 차원 출력 
print (p.shape) # 행렬 크기 출력 : tuple 형태로 
print (p.shape[0]) # 행렬 크기 중 row 크기 출력 

X = np.array ([1, 2]) # 입력층 배열
W = np.array ([[1, 3, 5], [2, 4, 6]]) # 가중치 배열 
Y = np.dot(X, W) # 행렬의 곱 계산 -> 다음 층의 weighted sum 계산
print (X)
print (W)
print (Y)
print (X.shape)
print (W.shape)
print (Y.shape)