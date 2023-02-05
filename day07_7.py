class student:
    name = ''
    num = 0
    tall = 0
    def __init__(self,name,num,tall):
        self.name = name
        self.num = num
        self.tall = tall

        # 예를 들어, 이 메서드가 버그가 있어서 수정해야 할 경우
    def 학생정보보기(self):
        print(f'이름: {self.name}, 번호: {self.num}, 키: {self.tall}')
    def 학생정보입력(self,name,num,tall):
        self.name = name
        self.num = num
        self.tall = tall

# 다른 사람들이 '학생 클래스 사용
# 클래스 업데이트 요청

# 상속 : 사람이 복붙을 하면 사람이 고쳐야하기 때문에, 컴퓨터가 복붙을 해서 컴퓨터가 고치게 한다(클래스 복붙)
class student2(student):
    pass
    # 학생 클래스의 변수와 메서드를 복붙 해줌
    def __del__(self):
        print('프로그램 종료')
    # 소멸자
    #객체 (변수)가 없어질 때 사용되는 함수
class student3(student):
    def 학생정보보기(self):
        print(f'==이름: {self.name}, 번호: {self.num}, 키: {self.tall}==')
        # 원본 클래스는 '부모 클래스',복붙받은 클래스는 '자식 클래스'
        # 만약에, 부모와 자식이 메서드명이 곂치면
        # 자신의 메서드가 우선으로 사용된다
a = student2('철수',1,177)
a.학생정보보기()

b = student3('짱구',2,183)
b.학생정보보기()
