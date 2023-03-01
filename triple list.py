def triple(n):
    return n*3

l=[]
n=int(input('Enter no. of elements : '))
for i in range(n):
    l.append(int(input('Enter number : ')))
    
print('List Has been Tripled :',list(map(triple,l)))