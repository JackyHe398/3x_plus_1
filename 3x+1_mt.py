import os
import threading


def job1(last):
    for i in range(last+1,last+1001,2):
        ct1 = i
        while not(ct1 == 1 or ct1 == 2 or ct1 == 4):
            if ct1%2 == 0:
                ct1 = ct1/2
            else:
                ct1 = 3*ct1+1
        print(i)

def job2(last):
    for i in range(last,last+1000,2):
        ct2 = i 
        while not(ct2 == 1 or ct2 == 2 or ct2 == 4):
            if ct2%2 == 0:
                ct2 = ct2/2
            else:
                ct2 = 3*ct2+1
        print(i)


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

while 1==1:
    last += 1000
    c = last
    t1 = threading.Thread(target = job1,args=(last,))
    t2 = threading.Thread(target = job2,args=(last,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    last = last - (last%1000)
    
    f2 = open(f'{__file__}\\..\\result1000.txt', 'r+')
    f2.write(str(last))
    f2.close()
    f1 = open(f'{__file__}\\..\\result.txt', 'r+')
    f1.write(str(last))
    f1.close()
    