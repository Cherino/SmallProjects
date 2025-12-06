import random

MYNAME = 'Caileb'
hello = ['H','e','l','l','o',' ','C','I','S','#']
hellocis = ''
for i in hello:
    if i == '#':
        for j in range(1703):
            if j == 1702:
                hellocis += '-'
                hellocis += str(j)
    else:
        hellocis += i
hellocis += '!'
print(hellocis)
#WOAH COMMENT
a, b = 7, 6
if a * b == 42:
    print('GOOD MATH', MYNAME)
print('random number time')
c = input('give a number')
d = input('give another number')
print("here's 5 random numbers within that range")
k = 0
while k != 5:
    print(random.randint(int(c),int(d)))
    k+=1