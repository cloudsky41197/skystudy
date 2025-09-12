# 반환타입 : O 매개변수 : 0 - 자판기
# 반환타입 : 0 매개변수 : X - 정수기
# 반환타입 : X 매개변수 : O - 쓰레기통
# 반환타입 : X 매개변수 : X - 마우스

def vendingmc(음료) :
    print(f'{음료}를 선택하셨습니다.')
    return(f'{음료}가 나왔습니다.')
print(vendingmc('사이다'))

def waterfountain():
    return('물')
print(waterfountain())

def trashcan(쓰레기) :
    print(f'{쓰레기}를 버렸습니다.')
trashcan('휴지')

def mouse():
    print('눌렀습니다.')
mouse()


