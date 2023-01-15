# list = []
# 리스트 : 변수들을 뭉쳐놓은것
# 
list = [1,2,3,4]
result = list.index(3)
print('해당 데이터가 저장되어있는 위치는 :', result)
# 0부터 시작
print(list[2])
# 추가 append
list.append(314)
print(list)

# 사이에 넣는것 '삽입'
list.insert(2,2222)
print(list)

# 수정
list[4] = 567

# 제거
list.remove(2222)
print(list)

# 뒤쪽부터 뽑기 pop
뽑기결과 = list.pop()
print(list)
print(뽑기결과)

# 리스트 비우기 clear
list.clear()
print(list)

# 리스트 합치기 extend
list2 = [1,2,3,4,5,6,7,8,9,10]
list.extend(list2)
print(list)

# 리스트 뒤집기 reverse
list.reverse()
print(list)

# count 
십의갯수 = list.count(10)
전체갯수 = len(list)
print(십의갯수)
print('전체 저장된 갯수는',전체갯수)

# 리스트 낮은 순서대로 정렬 sort
list.sort()                 # 기본적으로 낮은 순부터 정렬 (오름차순)
print(list)

# 현재 리스트를 보존하면서 테스트를 하고 싶다
test_list = list.copy()
print('기존 리스트를 보존하면서 복붙을 만듭니다: ',test_list)
# 전체 출력
for i  in list:
    print(i)