# 문자열을 저장하는 리스트
lst = []
num = 0
수정 = 0
수정하고자할값 = 0
삭제 = 0
# 사용자에게 입력을 받아 리스트를 구성
# 1: 추가하기, 2: 수정하기, 3: 삭제하기, 4: 전체보기

while True:
    num = int(input('1:추가, 2:수정, 3:삭제, 4:조회, 0:종료 >>'   ))
    if num == 1:
        lst.append(input('추가할 값 입력>>' ))
        print('현재 추가한 값',lst)
        print()      
    elif num == 2:
        print('현재 저장된 값',lst)
        수정 = int(input('수정할 위치를 입력해주세요 (1부터시작)>> '))
        수정하고자할값 = (input('수정할값을 입력하세요>>'))
        lst[수정-1] = 수정하고자할값
        print(수정,'번 위치 ''= ',수정하고자할값,'으로 변경되었습니다')
        print('현재 저장된 값',lst)
        print()
    elif num == 3:
        print('현재 저장된 값',lst)
        삭제 = input('삭제할 값을 입력하세요(같은값이면 중복제거)>>' )
        if 삭제 in lst:
            lst.remove(삭제)
            print(삭제,'제거 되었습니다')
            print()
            print('현재 저장된 값',lst)
            print()
        else:
            print()
            print('그 값은 저장되어있지 않습니다.')
            print('현재 저장된 값',lst)
            print()
    elif num == 4:
        for i in lst:
            print(i)
    elif num == 0:
        print('프로그램종료')
        break
    else:
        print('없는번호입니다')
        print()

