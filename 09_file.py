import random

number = random.randint(1,31) # 1~31 사이의 랜덤한 숫자

#number = random.randint(1,31)

print(f'내 마음속 숫자 : {number}')
#print(f'내 마음속 숫자 : {number}') # 복습 : f-string을 사용하면 문자열과 다른 타입의 데이터를 함께 출력할 수 있다.
# print(number)
running = True # 실행

while running: # 아래와 같을 경우 반복 실행...? # 무한루프 # 내가 생각한 숫자를 맞출 때까지 실행
    # 입력받은 값을 정수(int)로 변환하여 guess 에 대입
    guess = int(input('1~31 중 내가 생각한 숫자는?'))
    print(f'입력받은 숫자 : {guess}')

    if guess > number: # 랜덤한 숫자가 1~31 중 내가 생각한 숫자보다 작다면?
        print(f'{guess}보다 작습니다')
    # if guess #=int(input('1~31 중 내가 생각한 숫자는?)) > number :
        # print(f'{guess}보다 작습니다')
    elif guess < number: # 그게 아니라면, 랜덤한 숫자가 내가 생각한 숫자보다 크다면?
        print(f'{guess}보다 큽니다')
    else: # 그것 또한 아니라면, 이 숫자는 내가 생각한 숫자가 맞다.
        print('정답!')
        running = False # 실행 중지 # 정답을 맞췄으므로 더이상 실행을 할 필요 없음.

