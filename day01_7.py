#  연산자
a = 10
b = 3

a + b     
a%b #나머지구하기 1
a**b # a의 b 제곱
a = b # b를 a공간에 대입    오른쪽 값 왼쪽 공간
a == b # 같다 (수학의 = )
a >= b # a 가 b보다 크거나 같다

# 대입연산자 주의할 점 =
a = a # 이 두 a는 다름 왼쪽 a 는 공간 오른쪽 a 는 값
a == a #이 두  a는 같음

a += b   # a = a + b
a -= b
a *= b
a /= b 

a + b * a # "수학의 개념" (곱셈 먼저)

# 비교 연산자 ==, >=, >
a = 10
b = - 4
print(a != b)     # 10은 3과 다르다.    True or False 로 알려줌

#관계연산자 and, or, not

print(5 <   a < 15)                 #a는 5보다 크고 15보다 작다

# a는 0보다 작거나 5보다 크다

print(not a< 0)

