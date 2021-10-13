import math

numerator = int(input("Enter a numerator: "))
while True:
    if numerator <= 0:
        numerator = int(input("Please re-enter the numerator. Value must be greater than 0: "))
        continue
    else:
        break
    
denominator = int(input("Enter a denominator: "))
while True:
    if denominator <= 0:
        denominator = int(input("Please re-enter the denominator. Value must be greater than 0: "))
    else:
        gcd = math.gcd(numerator, denominator)
        num1 = numerator // gcd
        den1 = denominator // gcd
        if numerator < denominator:
            print(numerator, "/", denominator, "is a proper fraction.")
            if gcd == 1:
                print("This proper fraction cannot be reduced any further.")
                break
            else:
                print("This proper fraction can be reduced to : ", num1, "/", den1)
                if den1 == 1:
                    print("The whole number is", num1)
                    break
                else:
                    break


        else:
            print(numerator, "/", denominator, "is an improper fraction.")
            if gcd == 1:
                print("This improper fraction cannot be reduced any further.")
                a = num1 // den1
                b = int(num1 % den1)
                if den1 == 1:
                    print("The whole number is", num1)
                    break
                else:
                    print("The mixed number is", a, "and", b, "/", den1)
                    break
            else:
                print("This improper fraction can be reduced to: ", num1, "/", den1)
                a = num1 // den1
                b = int(num1 % den1)
                if den1 == 1:
                    print("The whole number is", num1)
                    break
                else:
                    print("The mixed number is", a, "and", b, "/", den1)
                break