n = int(input('Write a num of projects:\n'))
b = ['' for i in range(n)]
c = [0 for i in range(n)]
a = [['', ''] for i in range(n)]
r, p = [], []
print('Enter the name & progress:\n')
for i in range(n):
    b[i] = input('Name of project {0}: '.format(i + 1))
    c[i] = int(input('Progress of project {0}: '.format(i + 1)))
print('–––––––––––––––––––––––––––––––––––––––––\n\t\tAll projects:\n–––––––––––––––––––––––––––––––––––––––––')
print('\tName\t    | \tProgress')
print('--------------------|--------------------')
for i in range(n):
    a[i][0] = b[i]
    a[i][1] = str(c[i])
    x, y = a[i][0], a[i][1]
    if len(b) != i + 1:
        print('{0}\t\t    |{1}\t\n--------------------|--------------------'.format(x, y))
    else:
        print('{0}\t\t    |{1}\t\n–––––––––––––––––––––––––––––––––––––––––'.format(x, y))
    if c[i] >= 85:
        r.append(b[i])
        p.append(c[i])
if len(r) == 0:
    print('O-------------------O')
    print('| Nothing is ready! |')
    print('O-------------------O')
else:
    print('\t\t   Ready:\n–––––––––––––––––––––––––––––––––––––––––')
    for i in range(len(r)):
        if len(r) != i + 1:
            print('{0}\t\t    |{1}\t\n--------------------|--------------------'.format(r[i], p[i]))
        else:
            print('{0}\t\t    |{1}\t\n–––––––––––––––––––––––––––––––––––––––––'.format(r[i], p[i]))
