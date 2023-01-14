# 반복문 while(, for)

# for를 사용해서 hello 3번하기

# for 임시변수 in range(3):
#     print('hello')


# 임시변수 : while에서 i를 값으로 사용 ==> 임시변수

# i  = 0
# while i < 3:
#     print(i, '번째 Hello')
#     i +=  1


# for j in range(3):
#     print(j,'번쨰 Hello')

# # i = 1

# for i in range(1, 4):
#     print(i,'번째 hello')

# range(3) == range(0 ~ 2)                  
# range(1, 4) == 1 ~ 4전까지 (1~3)

# for i in range(1, 13):
#     print(i,'월')

# for i in range(7,101, 7):
#     print(i)


# 짝수만 출력하기
# for j in range(0, 11, 2):
#     print(j)


# 문제
'''
5
4
3
2
1

'''

# 문제2
'''
양의 정수 1개를 입력 받아서 
1부터 입력한 숫자까지 합계를 알려주는 프로그램 만들기

ex) 10
1 ~ 10을 모두 더해서 55
'''


# num = 5
# for i in range(5):
#     print(num)
#     num -= 1

# for i in range(5 , 0, -1):
#     print(i)



# i = int(input('정수 1개를 입력하세요>>'))
# a = 0
# b = 1
# for i in range(1, i+1):
#     a += b
#     b += 1
# print(a)

count = int(input('양의 정수를 입력하세요>> '))
sum = 0
for i in range(1, count + 1):
    sum += i
print(sum)

# 문제3 
# num1 = 1
# num2 = 2
# backup = 0
# backup = num1
# num1 = num2
# num2 = backup
# print(num1, num2)