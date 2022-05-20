import math

def sequence_parity(num):
    print("SEQUENCE PARITY ===============")
    print(" ")
    par = (-1)**num

    if par == 1:
        print("The number is even")
    else:
        if par == -1:
            print("The number is odd")

def div_parity(num):
    print("DIVISION PARITY ===============")
    print(" ")
    par = num%2
    if par == 0:
        print("The number is even")
    else:
        if par > 0:
            print("The number is odd")

num = 0

while num == 0:
    try:
        num = float(input("Insert an integer:  "))
        print(" ")
    except:
        print(" ")
        print("String inputs are not accepted.")
        print(" ")

if num.is_integer() == False:
    print("Unable to determine the parity of the number, please make sure that the number inserted is an integer. Your number will be rounded.")
    print(" ")
    num = int(num)
    print("Your number has been rounded to: " + str(num))
    print(" ")
print(" ")
sequence_parity(num)
print(" ")
print(" ")
div_parity(num)
print(" ")



