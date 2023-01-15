문자열 = 'Hello world, my name is python'
정수 = 314
실수 = 3.14

# for i in 문자열:
#     print(i, end=' ')

# i = 0
# while i < len(문자열):
#     print(문자열[i], end=' ')
#     i += 1



# 문제 : 문자열에서 알파벳 o의 갯수를 알렺우세요
문자열 = 'Hello world, my name is python'
a = 0
for i in 문자열:
    if i == 'o':
        a += 1
print(a)


month = int(input('1 ~ 12월중 아무 월이나 입력해보세요 (숫자만) >>>> '))
for i in range(1, 13):
    if i == month:
        continue
    print(i,'월',end=(' '))

for i in range(3):
    print()


월 = int(input('1 ~ 12월중 아무 월이나 입력해보세요 (숫자만) >>>> '))
for i in range(1, 월):
    print(i,'월')
print()
# str, int, float, list, tuple, dict, set
# 리스트
# 지하철 3칸, [10, 15, 12]
subway1 = 10
subway2 = 15
subway3 = 12
list = [10, 15, 12]
# list = 같은 주제의 변수들을 묶음으로 보관 (전체 출력이 가능)
for i in list:
    print(i,'명',end=(' '))
print()
for i in range(1, 11):
    for j in range(1, 11):
        print(i,'곱하기',j,'=',i*j,end=('     '))
    print()

for i in range(3):
    print()

for i in range(1, 11):
    print(i,'의 제곱 =',i*i*i,end=('   '))

    