def square(n):
    return n**2

l=[]
n=int(input('Enter no. of elements : '))
for i in range(n):
    l.append(int(input('Enter number : ')))
    
print('List Has been Squared :',list(map(square,l)))