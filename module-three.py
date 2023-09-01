import os 
os.system("cls"); 

# uppgift 1
user_input = input("Type in something :")

for x in range(0, 10): 
    print(user_input)


# uppgift 2
for x in range(0, 10): 
    print(x + 1)


# uppgift 3
y = input("range: (1, y), y: ")

for x in range(1, int(y) + 1):
    print(x)


# uppgift 4
for x in range(1, 13): 

    print(f"{x}ans tabell :")

    for y in range(1, 10):
        print(f"{x} * {y} = {x * y}")


# uppgift 5
base = int(input("enter the base number: "))
exponent = int(input("%s power in: " %(base)))

result = base # number entered by user.

for x in range(1, exponent):
    result = result * base

print("result is : %s" %(result))


# Miniräknare
def askNumbers(): 

    first_number = int(input("enter your first number :"))
    second_number = int(input("enter your second number :"))

    chooseOperation(first_number, second_number)


def chooseOperation(num1, num2):

    # Jag knyter här resultaten av varje operation med det siffran användaren anger
    operations = {"1" : num1 + num2, 
                  "2" : num1 - num2, 
                  "3" : num1 * num2, 
                  "4" : num1 / num2
                  }
    showOperations()

    user_operation_choice = input("type in a number of operation you want to perform: ")
    print(showAwnser(operations[user_operation_choice]))


def showOperations():
    operation_names = ["addition", "subtraktion", "multiplication", "devision"]
    
    for index in range(1, len(operation_names) + 1):
        print("%s - %s" %(index, operation_names[index - 1]))


def showAwnser(awnser):
    return awnser


askNumbers()
