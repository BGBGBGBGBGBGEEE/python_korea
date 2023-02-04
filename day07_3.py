# 클래스 : 함수 + 변수 ==> 메서드, 멤버변수

# 전역변수 
전역변수 = 1

def 함수(매개변수):
    지역변수 = 2


class 클래스:
    멤버변수 = 3
    def 메서드(self,매개변수):
        pass
# 변수의 범위
# 전역변수 : 생성되면 프로그램 종료될때까지 살아있음 (프로그램 성능을 떨어뜨릴 수 있음), 모든곳에서 사용가능
# 멤버변수 : 객체화하면 클래스가 사용되는 동안에는 살아있음, 객체를 통해서 사용가능
# 지역변수(매개변수) : 함수가 사용되는 동안에만 살아있음, 함수 안에서만 사용 가능

# 객체화 (클래스를 사용하기 위해 변수에 담는다, 이때 변수는 객체라고 지칭한다)
# 왜 클래스를 담은 변수만 객체라고 부르냐 : 메서드를 갖고 있는 변수
a = 클래스()
d = 3


# 변수 d는 파생되서 더 할 수 있는게 있지 않음
# 객체 a는 a를 통해서 매개변수와 메서드 사용이 가능
a.메서드
a.멤버변수

print(a.멤버변수) # a 객체는 그 안에 있는 것을 사용
print(d)        # d 변수는 그냥 사용


# 컴퓨터   >>> 주변 맥락을 이해해야 의도 파악이 가능
# 홍길동의 컴퓨터 >>> 그냥 봐도 이해가능 (홍길동에 대해서만 알면 됨)