# 함수 def
#함수의 목적 : 1. 가독성 2.코드 재활용
# 함수의 정의
def 내가만든함수():
    print('파라미터가 없는 함수, 리턴이 없는 함수')


def 내가만든함수(num1, num2):
    print('파라미터가 있고, 리턴은 없는 함수')
    print(num1, num2)
    지역변수 = '함수 안에서 새로만든 변수, 매개변수와 지역변수는 함수가 끝나면 없어짐'




def 내가만든함수(num):
    print('파라미터가 있고, 리턴이 있는 함수')
    result = abs(num)
    return result             # 내보낸다(return : 지역변수는 없어지기 때문에 외부에 값 전달하기 위한 방법)



# 함수의 사용 <<함수명>>
내가만든함수()
내가만든함수()