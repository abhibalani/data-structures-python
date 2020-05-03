# The criteria that must be met to create closure in Python are summarized in the following points.
#
# We must have a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.


def make_multiplier(n):

    def multiplier(x):
        return x*n

    return multiplier


times2 = make_multiplier(2)

print(times2(5))


times5 = make_multiplier(5)

print(times5(5))
