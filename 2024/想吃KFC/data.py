from random import randint

print('8')
print('10 7 10 2 9 9 3 3')
print()

for i in range(1, 11, 2):
    for _ in range(2):
        print(i)
        print(*(randint(1, 10) for _ in range(i)))
        print()

for _ in range(5):
    n = 10
    print(n)
    print(*(randint(7, 10) for _ in range(n)))
    print()
