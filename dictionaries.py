highscore = {
    'alice': 123,
    'bob': 234,
    'claire': 345,
}

phonenumbers = {
    'alice': '555-1234',
    'bob': '555-2345',
    'claire': '555-3456',
}

k1 = highscore.keys()
print(k1)
print(id(k1))
print(highscore.values())
print('-'*40)
k2 = phonenumbers.keys()
print(k2)
print(id(k2))
print(phonenumbers.values())