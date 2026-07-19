#Right angle piramid (star)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#Right angle piramid with same row 
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
#Right angle piramid with increasung row
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Reverse star piramid
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#Reverse right angle piramid with same row
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
#Reverse right angle piramid with increasing row
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#piramid
n = 5

for i in range(1, n + 1):

    
    for j in range(n - i):
        print(" ",end="")
        
    for j in range(2*i-1):
        print("*",end="")
    print()

#reverse pirmid
n = 5

for i in range(n,0,-1):

    
    for j in range(n - i):
        print(" ",end="")
        
    for j in range(2*i-1):
        print("*",end="")
    print()
#dimond shape
n = 5

for i in range(1, n + 1):

    
    for j in range(n - i):
        print(" ",end="")
        
    for j in range(2*i-1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):

    
    for j in range(n - i):
        print(" ",end="")
        
    for j in range(2*i-1):
        print("*",end="")
    print()

#butterfly
n = 5


for i in range(1, n + 1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

for i in range(n, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

#butterfly(updated)
    n = 5

for i in range(1, n + 1):
    
    for j in range(i):
        print("*", end="")
    
    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()
for i in range(n - 1, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

#half butterfly wing

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
#square
n=10
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

# X
n=7
for i in range(n):
    for j in range(n):
        if j==i or j+i==n-1:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()

        

#hallow
# Hollow square pattern

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


