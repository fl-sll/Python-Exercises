def primechecker(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
            else: 
                return True
    else:
        print("False!")
    
def reverse(n):
    rev = str(n)[::-1]
    rev1 = int(rev)
    if rev1 != n:
        if primechecker(rev1) == True:
            if primechecker(n) == False:
                print("False")
            else:
                print(n, rev1)
        else:
            print("False!")
    else:
        print("False!")

def emirpchecker(n):
    primechecker(n)
    reverse(n)

n = int(input("Enter a number: "))
emirpchecker(n)