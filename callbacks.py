names = ['Mischa', 'Sarah', 'Dario', 'Ibrahim']


def welcome(person):
    print(f'Hallo, {person}')


def see_off(person):
    print(f'Adieu, {person}')


def all_participants(f):
    for n in names:
        # ``f`` is called a "callback function".
        # The required "shape" (aka "signature") of the callback function is defined
        # by the following line, i.e. where it is called. In this case, the callback
        # function (``f``) is expected to be callable with a single string parameter.
        f(n)


all_participants(welcome)

all_participants(see_off)

# we can pass an anonymous/unnamed lamdba function as a callback, too
all_participants(lambda n: print(f'Hi five, {n}!'))
