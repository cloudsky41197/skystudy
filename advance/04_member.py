class Robot :

    # 생성자? 객체화할때 호출되는 함수의 일종으로
    # 객체화가 될 때 가장 먼저 호출된다.
    # self?

    def __init__(self):
       print('Robot이 복사될 때 제일 먼저 호출되는 멤버')

    def doIt(self):
        print('나는 Robot의 함수입니다.')

robot = Robot()
robot.doIt()