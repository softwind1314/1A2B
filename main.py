#!/usb/bin/python
TABLE = "123456789"

print('Hello world')


def gen_target(t):
    from random import sample
    g = sample(t, k=3)
    return g


def compare_target(t, guess):
    ''' Count the xA yB matches.'''
    a = 0
    for x, y in zip(t, guess):
        if x == y:
            a += 1
    ab = len(set(t) & set(guess))
    return a, (ab - a)


goal = gen_target(TABLE)

# print (goal)

print("123 " + str(compare_target(goal, "123")))
print("456 " + str(compare_target(goal, "456")))
print("789 " + str(compare_target(goal, "789")))

s = input()
print(compare_target(goal, s))

s = input()
print(compare_target(goal, s))
s = input()
print(compare_target(goal, s))
s = input()
print(compare_target(goal, s))
s = input()
print(compare_target(goal, s))
s = input()
print(compare_target(goal, s))

print(goal)
