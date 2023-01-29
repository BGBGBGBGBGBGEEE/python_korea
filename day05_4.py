# 3개 더하기, 빼기, 곱하기, 나누기
# +, -, *, / : 2개만 할 수 있음


# lst = [10,20,30,40,50]
# sum = 0
# def 총합(lst):
#     a = 0                                         함수 안에서 만든 변수는 함수가 끝나면 사라진다(지역변수)
#     for i in lst:
#         a += i
#     return a

# sum = 총합(lst)
# avg = int(sum/len(lst))

# print('총합',sum)
# print('평균',avg)


num = int(input('별의 갯수를 입력하세요>>> '))
def star(num):
    a = ''
    for i in range(num):
        a += '*'
    return a
        
    
        
a = star(num)

print(a)