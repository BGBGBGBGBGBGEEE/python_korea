# 함수 : 코드를 묶는기술(코드 재활용)
# 반복문도 코드를 묶는 기술(붙어있는 코드만 가능) [i라는 임시변수를 통해서 코드 변화에 대처]
# 함수 : ()를 통해서, 파라미터를 통해서, 코드변화에 대처
# 함수의 정의 : def 라는 키워드로 할 수있음

def 이름출력(name):
    print(name) # 이름출력
    return name # 다시 돌려준다, ()로 받았으면 return 으로 돌려준다


이름출력('홍길동')

result2 = 이름출력('이순신')  # return이 존재하면 함수를 변수에 대입하는 것 같은 형태로 사용

