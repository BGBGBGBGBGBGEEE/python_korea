import matplotlib.pyplot as plt      # 그래프 그려주는 라이브러리



# 문제 : 80점 이상인 사람의 수
시험점수 = [71,85,77,81,99,23,55,100,0]
_80점이상 = []

for i in 시험점수:
    if i >= 80:
        _80점이상.append(i)
갯수 = len(_80점이상)
print(갯수)

# 데이터 시각화
plt.hist(시험점수)
plt.title('test')
plt.xlabel('score')
plt.ylabel('person')            # 막대그래프
plt.show()                      # 그려줘














