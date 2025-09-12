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

# 사전의 특정 요소를 꺼내보자(사용법은 Lsit 와 비슷하다.)
print(dic2['name'])
print(dic2['friends'])
print(dic['phone'])
# get 메서드를 활용해서도 가져올 수 있다.
print(dic2.get('phone'))
print(dic.get('nick'))
# 특정 키가 없는 경우 None 이 아닌 대체 내용으로 반환할수 있음
print(dic2.get('nick','해당 내용이 없음'))