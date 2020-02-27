#!/usb/bin/python
TABLE = "123456"

'''
import random
goal = random.sample(TABLE, k=2)

def same_pair(p):
    return 1 if p[0]==p[1] else 0

#m = map(same_pair, zip(goal, input()))

aa = [ a[0]==a[1] for a in zip(goal, input())]

print(aa)

print(aa.count(True))
#next(m)
#for i in m:
#    print(i)

import sys
sys.exit(0)
'''

def gen_target(t):
    from random import sample
    g = sample(t, k=2)
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

print("12 " + str(compare_target(goal, "12")))
print("34 " + str(compare_target(goal, "34")))
print("56 " + str(compare_target(goal, "56")))

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
