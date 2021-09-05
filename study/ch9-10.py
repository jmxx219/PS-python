# 함수
def make_sound(): # 함수 정의
    print('quack')


def echo(anything): # 반환값
    return anything + ' ' + anything


def whatis(thing): # None
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


def menu(wine, entree, dessert='pudding'): # 기본 매개변수 값 지정
    return {'wine' : wine, 'entree' : entree, 'dessert': dessert}


def buggy(arg, result=[]): # 일반 매개변수: arg, 기본 매개변수: result
    result.append(arg)
    print(result)


def nonbuggy(arg, result=None): # 일반 매개변수: arg, 기본 매개변수: result
    if result is None:
        result = []
    result.append(arg)
    print(result)


def outer(a, b): # 내부 함수
    def inner(c, d):
        return c + d
    return inner(a, b)


def edit_story(words, func):
    for word in words:
        print(func(word))
   
        
def fn(x: int) -> bool:
    a: str = 1
    print(type(a))


def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


def generator():
    yield 1
    yield 'string'
    yield True


class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


if __name__ == '__main__':
    make_sound() # 함수 호출
    print(echo('jimin'))
    whatis(None)
    whatis(True)
    print(menu('frontenac', dessert = 'flan', entree = 'fish'))
    print(menu('chardonnay', entree = 'fish'))
    buggy('a') # ['a']
    buggy('b') # ['a', 'b'] -> 이전에 호출했던 result가 그대로 리스트에 남아있음
    nonbuggy('a') # ['a']
    nonbuggy('b') # ['b']
    print(outer(1, 2))

    # 람다함수(익명함수)
    stars =['thud', 'meow']
    edit_story(stars, lambda word: word.capitalize() +'!')

    # 제너레이터
    g = get_natural_number()
    for _ in range(0, 100):
        print(next(g), end=" ") # next()로 다음 값을 추출

    print("")
    gen = generator()
    print(next(gen), end=" ")
    print(next(gen), end=" ")
    print(next(gen), end=" ")
    print("")

    # enumerate
    a = [1, 2, 3, 2, 45, 2, 5]
    print(a)
    print(enumerate(a))
    print(list(enumerate(a)))

    for i, v in enumerate(a):
        print(i, v) #인덱스와 값 함께 출력

    # 믹스인 클래스
    t = Thing()
    t.name = "Jimin"
    t.age = 21
    t.dump()