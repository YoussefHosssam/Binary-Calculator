# ---------------------- check validity -------------------
def validity (num) :
    x = 0
    while True :
        if num.isalpha() == True or int(num) < 0 :
           num = input("Please, insert a valid binary number : ")
        else : break 
    while x < int(len(num)) : #check valid of binary num
        if num.isalpha() == True or int(num[x]) > 1 or int(num[x]) < 0 :
            num = input("Please, insert a valid binary number : ")
            x = -1
        x+=1
    return num
# ---------------------- check validity -------------------
# ---------------------- make number 8 digits  -------------------        
def eightdigits (num) :
    while len(num) < 8 :
        num = "0" + str(num)
    return num    
# ---------------------- make number 8 digits  -------------------
# ---------------------- Convert to decimal from binary  -------------------
def binarytodecimal (num) :
    decimal = 0
    x = 0
    while x < len(num) :
        decimal += (2**(len(num)-1-x))*int(num[x])
        x+=1
    return decimal     
# ---------------------- Convert to decimal from binary  -------------------
# ---------------------- Convert to binary from decimal  -------------------
def DecimalToBinary(num):
    if num >= 2:
        return str(DecimalToBinary(num//2)) + str(num%2)
    elif num == 1 : return 1
    elif num == 0 : return 0
# ---------------------- Convert to binary from decimal  -------------------
# ---------------------- one's complement  -------------------
def ones_complement (num) :
    num = ''.join('1' if bit == "0" else "0" for bit in str(num))
    return num
# ---------------------- one's complement  -------------------
# ---------------------- Addition  -------------------
def binary_addition(num1, num2):
    result = []
    carry = 0
    for i in range(len(num1) - 1, -1, -1):
        sum = int(num1[i]) + int(num2[i]) + carry
        result.insert(0, str(sum % 2))
        carry = sum // 2
    if carry:
        result.insert(0, str(carry))
    return ''.join(result)
# ---------------------- Addition  -------------------
# ---------------------- Subtraction  -------------------
def binary_subtraction(num1 , num2):
    result = []
    borrow = 0
    for i in range(len(num1) - 1, -1, -1):
        sub = int(num1[i]) - int(num2[i]) - borrow
        result.insert(0, str((sub + 2) % 2))
        borrow = 1 if sub < 0 else 0
    return ''.join(result)
# ---------------------- Subtraction  -------------------
# ---------------------- Menu -------------------
def menu1 () :
    while True : #Menu1
        menu1 = input("** binary calculator **\nA)Insert new numbers\nB)Exit\n")
        if menu1 == "A" :
            global number1
            number1 = input("Please,insert the first binary number : ")
            number1 = validity(number1) #checking validity of the first binary number
            number1_8digits = str(eightdigits (number1)) #make the first binary number 8 digits
            while True : #Menu2
                menu2 = input("** please select the operation **\nA)Compute one's complement\nB)Compute two's complement\nC)Addition\nD)Subtraction\n")
                if menu2 == "A" : #calculate one's complement
                    print("The One's complement result is :" , ones_complement(number1_8digits) , "\n")
                    break
                elif menu2 == "B" : #calculate two's complement
                    print("The Two's complement result is :" , binary_addition("00000001" , ones_complement(number1_8digits)) , "\n")
                    break
                elif menu2 == "C" : #binary addition
                    number2 = input("Please,insert the second binary number : ")
                    validity(number2)
                    number2_8digits=eightdigits(number2)
                    addition = binary_addition(number1_8digits , number2_8digits)
                    print("The Addition result is :" , addition , "\n")
                    break
                elif menu2 == "D" : #binary subtraction
                    number2 = input("Please,insert the second binary number : ")
                    number2 = validity(number2)
                    number2_8digits=eightdigits(number2)
                    subtraction = binary_subtraction(number1_8digits , number2_8digits)
                    print("The Subtraction result is :" , subtraction , "\n")
                    break
                else : print("Please, select a valid choice")                
        elif menu1 == "B" : break #exit
        else : print("Please, select a valid choice") #invalid choice
menu1()    
# ---------------------- Menu -------------------



# Youssef Hossam Ibrahim Abbas  - 20230490
# Ziad El-sayed Mohamed Mahmoud - 20230152
# Youssef Ayman Byoumi Radwan   - 20230483