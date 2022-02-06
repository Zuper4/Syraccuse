print("\nThis program will applicate the theory of syraccuse.")
print("If the number is even, we divide it by 2.")
print("If the number is odd, we multiply it by 3 and we add 1.")
print("If we reach the number 1, the program stops.")
print("The theory of syracuse suppose that EVERY number you choose at the begining,")
print("It will ALWAYS reach the number 1 !")

try:
    number = int(input("enter a number: "))
    result = []
    while number != 1:
        if number % 2 == 0:
            number /= 2
            result.append(round(number))

        elif number % 2 == 1:
            number *= 3
            number += 1
            result.append(round(number))
            
    print(result)
    print("It got to the number 1 in " + str(len(result)) + " steps !")

except:
    print("Please put a number !!")
