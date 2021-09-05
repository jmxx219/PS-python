# 튜플 - 불변
empty_tuple = () # 생성
one_marx = 'gi', # 한 요소 이상의 튜플 생성에는 각 뒤에 ,(콤마)를 붙인다.
one_marx = ('gi',) # 괄호 안에 콤마를 생략하면 문자열이 됨
print(one_marx)
print(type(one_marx))

marx_tuple = 'hi', 'hello', 'ah'
marx_tuple = ('hi', 'hello', 'ah')
print(marx_tuple) # 요소가 두 개 이상이면 콤마 사용 x

a, b, c  = marx_tuple # 한 번에 여러 변수를 할당 -> 튜플 언패킹
print(a, b, c)

# 값 교환에서 임시변수 사용하지 않고 가능
a = '0'
b = '1'
print(a, b)
a, b = b, a
print(a, b)

marx_list = ['hi', 'hello', 'ah']
print(tuple(marx_list)) # tuple() : 다른 객체를 튜플로
print(('hi',) + ('hello', 'ah')) # 결합 : +
print(('ah',) * 3) # 복제 *

# 리스트 - 가변
empty_list = [] # 생성
another_list = list()  # list() 함수로 빈 리스트 생성
print(list('cat')) # list() : 다른 데이터 타입(튜플, 문자열, 셋, 딕셔너리 등)을 리스트로 변환

#리스트 컨프리헨션
num = [n for n in range(1, 6) if n % 2 == 1]
print(num)