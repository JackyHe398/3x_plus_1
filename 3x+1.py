import os
print(os.getcwd())
if not(os.path.isfile(f'{__file__}\\..\\result.txt') and os.path.isfile(f'{__file__}\\..\\result1000.txt')):
    f1 = open(f'{__file__}\\..\\result.txt', 'w+')
    f2 = open(f'{__file__}\\..\\result1000.txt', 'w+')
    f1.close()
    f2.close()

f1 = open(f'{__file__}\\..\\result.txt', 'r+')
f2 = open(f'{__file__}\\..\\result1000.txt', 'r+')
f1v = f1.readline()
f2v = f2.readline()
f1.close()
f2.close()


if f1v.isnumeric():
    print('f1')
    print(int(f1v))
    last = int(f1v)
elif f2v.isnumeric():
    print('f2')
    last = int(f2v)
else:
    last = 1
print(f'\'{last}\'')

    
print(f'last calculate: {last}')
c = 0
c = last

while 1==1:
    last += 1
    c = last
    while not(c == 1 or c == 2 or c == 4):
        if c%2 == 0:
            c = c/2
        else:
            c = 3*c+1
    print(last)
    if last % 1000 == 0:
        f2 = open(f'{__file__}\\..\\result1000.txt', 'r+')
        f2.write(str(last))
        f2.close()
    f1 = open(f'{__file__}\\..\\result.txt', 'r+')
    f1.write(str(last))
    f1.close()