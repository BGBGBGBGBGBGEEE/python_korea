# 내장함수 : 파이썬 내장 함수 (파이썬 언어에서 제공하는 기능)

# eval() : 문자열 형태의 연산식을 숫자로 계산

result = eval('5+5')
print(result)




# format() : 문자열 전환
result = format(1000000000,',')
# type() : 변수의 자료형태를 알려줌 
print((result))

print(type(123))


# str() : 문자열로 변환

# int() : 정수로 변환

# float() : 실수로 변환


# list(), tuple(), set(), dict() : 형변환

lst = [1,2,3]
print(tuple(lst))

# max()  최댓값
result = max(lst)
print(result)


# min()
"최솟값"

# sum()        전체 합계


# len(): 저장된 갯수


# abs()   절댓값


# pow()   제곱승
# 10^3 
pow(10,3)

# divmod() : tuple(몫, 나머지)
result = divmod(10,3)
print(result)

# round()   반올림
# 3.141592 둘쨰짜리까지 반올림
round(3.141592, 2)

# enumerate


def 포우(num1,num2):
    a = 1
    for i in range(num2):
        a *= num1
    return a
print(포우(10 , 3))

print(포우(12,2))


# range(n) : 0부터 n-1까지 반복 (n번 반복)
# range(n , m) : n ~ m -1 까지 반복 ( m- n 번 반복)
# range(n,m,x) : n ~ m-1 까지 반복을 하되, 간격을 X 만큼 뛰면서 (기본값 1)



for i in range(3):
    print('3번 반복',i)

for i in range(1,3):
    print('3-1번 반복',i)


for i in range(1,10,2): # 간격 2만큼 뛰면서 기본값 1  1 3 5 7 9
    print(i)


# sorted() : 리스트를 오름차순으로 정렬
lst = [3,4,1,2,7,6,9]

print(sorted(lst))

# 내림차순
print(sorted(lst, reverse = True))