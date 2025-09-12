# 사전은 키 : 값 형태로 되어있다.
# 비슷한 자료구조로는 자바 스크립트의 오브젝트, 자바의 맵이 있다.
dic = {
    'name':'kim,jin-hui',
    'phone':'010-1234-1234',
    'age': 28,
    'friends' : ['Alice','John','Smith']
}


dic2 = {
    'name':'hong,gil-dong',
    'phone':'010-1234-1234',
    'friends' : ['Alice','John','smith']
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)
# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)