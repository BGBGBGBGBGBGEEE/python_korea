# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot
#수학/과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
print(sklearn.__version__)

# 데이터를 가져온다 csv
원본데이터 = pd.read_csv('sample.csv', encoding='cp949')
print(원본데이터.head())

X = 원본데이터.iloc[:,:-1].values
y = 원본데이터.iloc[:,:-1]

print(X)
print(y)

선형기계학습 = LinearRegression()
# fit을 사용하면 기계학습을 한다 (모델 생성)
선형기계학습.fit(X, y)
print()
# predict 학습한 내용을 바탕으로 예측을 해
y_pred = 선형기계학습.predict(X)
print('예측한 y값:\n', y_pred)
# 학습한 내용을 바탕으로 예측을 해

print('AI예측한 값:',선형기계학습.predict[[(4.5)]])
print('AI예측한 값:',선형기계학습.predict[[[6.5],[9]]])

# 점찍기

plt.scatter(X,y,color='green')
plt.plot(X,y_pred, color='red')
plt.title('title')
plt.xlabel('xtitle')
plt.ylabel('ytitle')
plt.show()
