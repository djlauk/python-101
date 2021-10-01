def make_adder(increment_by):
    def inner_func(x):
        return x + increment_by
    return inner_func


# exactly the same, but using an anonymous 'lambda function'
# as the inner function to be returned
def make_adder_lambda(increment_by):
    return lambda x: x + increment_by


foo = make_adder(10)
bar = make_adder(100)

print(foo(5))
print(bar(5))
