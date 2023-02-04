# 학생 클래스
# 속성(멤버변수) 이름, 번호, 키
# 기능(메서드) : 학생정보보기


class student:
    name = ''
    num = 0
    tall = 0
    def __init__(self,name,num,tall):
        self.name = name
        self.num = num
        self.tall = tall
    def 학생정보보기(self):
        print(f'이름: {self.name}, 번호: {self.num}, 키: {self.tall}')
    def 학생정보입력(self,name,num,tall):
        self.name = name
        self.num = num
        self.tall = tall

        













# 사용예시
철수 = student('김철수',1,177.7)
영희 = student('박영희',2,155.5)
짱구 = student('신짱구',3,173.3)

철수.학생정보보기()
영희.학생정보보기()
짱구.학생정보보기()

짱구.학생정보입력('짱구',4,174.0)
짱구.학생정보보기()