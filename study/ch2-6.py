
# help('keywords') # 파이썬 예약어
print(type(7))  # 타입 값
print(type(7) == int)
print(isinstance(7, int))  # 특정 타입의 객첼르 가리키는지 확인


two = deux = zwei = 2  # 여러 이름 한꺼번에 할당
print(two, deux, zwei)


x = 5  # 불변 객체
y = x
x = 29
print(x, y)

a = [2, 3, 4]  # 가변 객체
b = a
a[0] = 99
print(a, b)


# bool 함수
print(bool(1))
print(bool(0))

print(1, 000, 000)  # 튜플(1, 000, 000)
million = 1_000_000  # 언더바(_)로 숫자 구분, 출력할 때는 무시
print(million)

print(9/5)  # 0으로 나누면 예외발생
print(9//5)  # 소수점 이하 버림
print(divmod(9, 5))  # 몫과 나머지 동시에 (1, 4)

print(2**3)
print(2.0**3)

# 리터럴 정수: 2진수(0b), 8진수(0o), 16진수(0x)
print(10)
print(0b10)
print(0o10)
print(0x10)


print(chr(65))  # chr() : 정수 -> 단일 문자열
print(ord('A'))  # ord() : 단일 문자열 -> 정수

# 부동소수점 숫자
print(float(98))  # 정수 -> 부동소수점 숫자
print(float('1.0e4'))

# 라인 유지
sum = 1 + \
    2
print(sum)


# if/else
furry = False
large = True
if furry:
    if large:
        print("yeti")
    else:
        print("cat")
elif large:
    print("ohoh")
else:
    print("ahah")
print("")

# 비교 연산자: == != < <= > >=
x = 7
print(5 < x and x < 10)
print(5 < x < 10)
print(5 < x or x < 10)
print(not 5 < x)
print("")

# in
letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
vowel_string = "aeiou"
vowel_dict = {'a': 'apple', 'e': 'elephant',
              'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}

print(letter in vowel_set)
print(letter in vowel_list)
print(letter in vowel_tuple)
print(letter in vowel_string)
print(letter in vowel_dict)

# 문자열
print(str(98.6))  # 문자열 타입으로 변환

# 이스케이프 문자: \n(줄바꿈), \t(공백)
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

test = "\"Ah\""
print(test)
print("A \\ B")  # 백슬래시 입력 -> 두 번 사용

print('hello' + 'world')
print("hello" "world")

start = 'Na' * 4 + '\n'  # 복제 *
print(start)

letters = 'hello'
print(letters[-1])  # 문자 추출 []

# 문자열은 불변 -> 특정 인덱스에 문자를 삽입 or  변경 X
temp = letters.replace('h', 'H')
print(letters)  # replace는 letters 자체를 바꾸지 않는다. 결과만 출력
print(temp)

# [:], [start :], [: end], [start : end], [start : end : step], [::step], [start::step]
# [::-1] : end ~ start 순서대로

print(len(letters))  # len() : 문자열 길이
print(letters.split('e'))  # split() :  문자열 나누기
print(', '.join(vowel_list))  # join() : 문자열 결합
print(letters.replace('he', 'ah'))  # replace() : 문자열 대체
world = " earth...!?"
print(world.strip())  # strip() : 문자열 스트립 - 공백 문자를 양쪽에서 제거
print(world.strip('.!?'))

# 검색, 선택
print(poem.startswith('All'))
print(poem.endswith('no doubt.'))
print(poem.find('the'))  # 없으면 -1 반환
print(poem.index('the'))  # 없으면 예외 발생
print(poem.count('the'))
print(poem.isalnum())

# 대소문자
setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())  # 첫 번째 단어를 대문자로
print(setup.title())  # 글자를 모두 대문자로
print(setup.lower())  # 글자를 모두 소문자로
print(setup.swapcase())  # 대 -> 소, 소 -> 대

# 문자열 정렬
print(setup.center(30))  # 문자열 중앙 정렬
print(setup.ljust(30))  # 문자열 왼쪽 정렬
print(setup.rjust(30))  # 문자열 오른쪽 정렬


# 포매팅 (% | {}, format() | f-문자열)

# 1. 옛 스타일  - %
print('%s' % 42)  # 문자열
print('%d' % 42)  # 10진수
print('%x' % 42)  # 16진수
print('%o' % 42)  # 8진수
print('')
print('%s' % 7.03)  # 문자열
print('%f' % 7.03)  # 10진 부동소수점
print('%e' % 7.03)  # 지수로 나타낸 부동소수점
print('%g' % 7.03)  # 10진 or 지수로 나타낸 부동소수점
print('%d%%' % 100)  # 리터럴 %
print('')
name = 'jimin'
print("My name is %s" % name)

# 2. 새 스타일 - {}, format()
thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))
print('The {1} is in the {0}.'.format(place, thing))
print('The {thing} is in the {place}.'.format(place='bathtub', thing='duck'))

# 3. 최신 스타일 - f-문자열
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')