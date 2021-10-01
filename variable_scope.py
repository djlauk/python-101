a = 11
b = 22


def alpha(a):
    # a = 99
    # global b
    b = a * 2
    print(f'in alpha, a = {a}, b= {b}')
    def beta():
        print(f'in beta, a = {a}, b = {b}')
        def gamma(a):
            print(f'in gamma, a = {a}, b = {b}')
        gamma(a * 3)
    beta()



alpha(1111)
alpha(3333)
