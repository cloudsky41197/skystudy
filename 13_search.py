#검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것
a = [3,4,1,2,3,4,'G','F,','G']
# 원하는 값의 인덱스 찾기
# 2 라는 값은 어느 위치에 있는가?
print(f'2는 어디?:{a.index(2)}')
print(f'G는 어디?:{a.index("G")}') # G는 2개이지만 처음 찾은 값만 알려준다.
# 5번 인덱스부터 'G'를 찾아라
print(f'G는 어디?:{a.index('G',5)}')


# 값이 없으면 에러(예외)를 발생시킨다.
#print(a.index('H'))#ValueError:'H'is not in list

b = [3,4,1,2,3,4,5,6,1,3,2] # 모든 3을 찾아 보세요.
# print(f'3의 값은 {b.index(3,0)}번에 있다.')
# print(f'3의 값은 {b.index(3,1)}번에 있다.')
# print(f'3의 값은 {b.index(3,5)}번에 있다.')

#코드리뷰#
#3이라는 값이 어느 위치에 있는지 + n번 인덱스부터 3을 찾아라
#-> b라는 리스트 안에서 3이 몇번 방에 있는지 보여주는 코드
# print(f'3는 어디?:{b.index('3',idx)}')

# idx = 0 # 0번부터 확인을 시작하기 위해
# while True: #멈추지 않고 무한으로 돌리기 위해 #오른쪽 구문이 사실일 경우 처음으로 돌아가 다시 시작
#     idx = b.index(3,idx) #0번 인덱스부터 시작해 몇번째 방에 3이 있는지 그 값이 idx자리에 담김 (value,start)니까...
#     print(f'3의 값은 {idx}번에 있다')
#     idx += 1 # 찾은 idx값으로부터 1을 더해서 다시 시작, 모든 3을 찾은 경우 더이상 3을 찾을 수 없으니 에러로 이어짐





for n in b : # for in 을 이용하면 list에 있는 값을 순서대로 하나씩 뽑아낸다.
    if n == 3:
        print(f'3이 있는 인덱스 : {idx}')
    #print(f'{idx}:{n}')
    idx += 1

# 리스트 요소 삭제
# del a[3]과 a.remove(3)
# del 은 특정 인덱스의 값을 지운다.
# remove 는 해당 값을 지운다.(한개만)
print(f'a : {a}')
a.remove(3)
print(f'a : {a}')

# pop() = append()의 반대개념
# 맨마지막 요소를 빼낸다. (리스트에서는 사라진다.)
val = a.pop()
print(f'빼낸 값 : {val}/a:{a}')
val = a.pop()
print(f'빼낸 값 : {val}/a:{a}')

# 리스트 확장 (더하기와 비슷한 개념)
print(a)
a.extend(b)
print(a)

#count(val) 특정한 값이 해당 리스트에 몇개 있는지 확인
print(a)
print(f'a안에 3은 {a.count(4)}개가 있다.')
print(f'a안에 9은 {a.count(9)}개가 있다.') # 없는 값은 0을 반환

# a 안에 있는 모든 3을 지워주세요. = a 안의 3을 ....

# print(f'a : {a}')
# a.remove(3)
# print(f'a : {a}')
# a.remove(3)
# print(f'a : {a}')
# a.remove(3)
# print(f'a : {a}')
# a.remove(3)
# print(f'a : {a}')
#
# print(a.index('3'))#ValueError:'3'is not in list

# idx = 0
# for n in a : # for in 을 이용하면 list에 있는 값을 순서대로 하나씩 뽑아낸다.
#     if n == 3:
#         a.remove(3)
#     print(a)

#print(f'a안에 3')

while True :
    a.remove(3)
    if a.count(3) == 0:
        break
print(a)








