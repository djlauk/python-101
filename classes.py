class Person:
    def __init__(self, name, favourite_color):
        self._name = name
        self.__favourite_color = favourite_color

    def __str__(self):
        return f"I'm {self._name}, and I like {self.__favourite_color}"

    def greet(self, other):
        print(f"Hi {other._name} I'm {self._name}")


class Superhero(Person):
    def __init__(self, name, lieblingsfarbe, super_power):
        Person.__init__(self, name, lieblingsfarbe)
        self._super_power = super_power

    def __str__(self):
        return f"I'm {self._name}, and I'm a super hero (power = {self._super_power})!"


batman = Superhero('Batman', 'black', 'technology')
robin = Person('Robin', 'red')


print(batman)
print(robin)
batman.greet(robin)
print(Person.__str__(batman))