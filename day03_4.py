# 기타 제어문
# break, continue

# break : 반복문 강제종료
# continue : 반복문이 안끝났어도 위로 올라감 (1회성 건너뛰기, 밑에 있는 코드는 무시)

# for i in range(10):
#     print((i+1),'번째 Hello')
#     if i == 2:
#         break

for i in range(1, 11):
    if i >= 4 and i < 8:
        continue
    print((i),'번째 Bye')