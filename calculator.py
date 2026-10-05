# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add(numOne, numTwo):
    return numOne + numTwo

def subtract(numOne, numTwo):
    return numOne - numTwo

def multiply(numOne, numTwo):
    return numOne * numTwo

def divide(numOne, numTwo):
    try:
        return numOne / numTwo
    except ZeroDivisionError:
        return 0

def powerOf(numOne, numTwo):
    return numOne ** numTwo


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    # Ask the user for a number
    #   -> Verify it's a number
    # Ask the user for an operation
    #   -> Verify it's a valid operation
    # Ask the user for another number
    #   -> Verify it's a number
    # Do some math
    # Give the answer
    # Prompt another equation

    calcOn = True
    operations = {"^": powerOf,
                  "*": multiply,
                  "/": divide,
                  "+": add,
                  "-": subtract}

    while calcOn:
        # Get and verify first num
        validFirstNum = False
        while not validFirstNum:
            print("")
            print("Enter your first number:")
            firstNum = input(" --> ")

            try:
                firstNum = float(firstNum)
                validFirstNum = True
            except ValueError:
                print("")
                print("That's not a valid number! Try again.")


        # Get and verify operator
        validOperation = False
        while not validOperation:
            print("")
            print("Enter an operation:")
            operator = input(" --> ")

            if operator in operations.keys():
                validOperation = True
            else:
                print("")
                print("That's not a valid operator! Try again.")


        # Get and verify second num
        validSecondNum = False
        while not validSecondNum:
            print("")
            print("Enter your second number:")
            secondNum = input(" --> ")

            try:
                secondNum = float(secondNum)
                validSecondNum = True
            except ValueError:
                print("")
                print("That's not a valid number! Try again.")


        # Do some math
        result = operations[operator](firstNum, secondNum)

        # Print the result
        print("")
        print(f"{firstNum} {operator} {secondNum} = {result}")



        print("")
        print("Would you like to perform another equation?")
        keepGoing = input(" --> ").lower()

        if keepGoing in ["no", "n", "quit", "exit"]:
            calcOn = False



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
