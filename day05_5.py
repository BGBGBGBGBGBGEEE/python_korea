# 외부 함수를 사용하는 법 : import

# 모듈 : 부품
# improt 모듈명

# import 모듈명
# import 모듈명 as 별명
# from 모듈명 import 함수명


import matplotlib.pyplot as plt
# 모듈 중에 font_manager와 rc만 가져옴
from matplotlib import font_manager, rc

font = font_manager.FontProperties(fname='gulim.ttc').get_name()
rc('font', family=font)
lst = [10,20,30,40,50,60,70,80,90,100]
plt.title('분포도')             # 제목 써줘
plt.xlabel('점수')
plt.ylabel('갯수')
plt.hist(lst)                # hist = 막대 그래프 그려줘
plt.show()