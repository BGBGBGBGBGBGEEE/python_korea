lst = ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']

# 리스트를 나누고싶다
# 1 ~ 6월 상반기
# 7 ~ 12월 하반기

# 리스트 슬라이싱
상반기 = lst[0:6]
print(상반기)

하반기 = lst[6:12]
print(하반기)

전체 = 상반기 + 하반기
print(전체)

print(lst[3:6])           # 슬라이싱