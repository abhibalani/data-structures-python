import functools


def outer(func):

    def inner():
        pass


class Test:

    def _abcd(self):
        print(1)
        return 1


Test._abcd(Test())


a = [1,2,3,4,5,6]

def square(x):
    return x*x


x = map(lambda z: z*z, a)

for i in x:
    print(i)

y = functools.reduce(lambda x, y: x+y, a)
print('Reducing ')
print(y)

z = filter(lambda x: x > 3, a)

for i in z:
    print(i)


def token_required(func):

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        print('Decorated')
        print('Arg is: ')
        print(args[0])
        func(*args, **kwargs)
        print('after the func')
        return
    return decorated


# @token_required
def myfunc(x):
    print("Calling my func")


func = token_required(myfunc)

func(19)