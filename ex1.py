def duplicate(x):
    return x + x


def triplicate(x):
    return x + x + x


print('----------')
print('step 1')

foo = 'hallo'
bar = 5
print(foo)  # output 1.1
print(bar)  # output 1.2
print(duplicate(foo))  # output 1.3
print(duplicate(bar))  # output 1.4

print('----------')
print('step 2')
bar = '5'
print(foo)  # output 2.1
print(bar)  # output 2.2
print(duplicate(foo))  # output 2.3
print(duplicate(bar))  # output 2.4

print('----------')
print('step 3')
bar = duplicate
duplicate = triplicate
print(duplicate(foo))  # output 3.1
print(bar(foo))  # output 3.2
print(duplicate(bar))  # output 3.3
