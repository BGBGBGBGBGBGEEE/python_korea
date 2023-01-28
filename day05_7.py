import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print(sklearn.__version__)

print('사이킷런 버전:',sklearn.__version__)

운동시간 = [0,1,2,3,4,5,6,7,8,9]
근육량 = [0,1,2.5,5,6.5,7,7.5,7.8,8,8.1]

lin = LinearRegression()
# 인공지능 학습 fit(X, Y)
lin.fit(운동시간, 근육량)
근육량예측 = lin.predict(운동시간)

plt.scatter(운동시간, 근육량)