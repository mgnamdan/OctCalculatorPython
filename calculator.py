# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add(numOne, numTwo):
    return str(float(numOne) + float(numTwo))

def subtract(numOne, numTwo):
    return str(float(numOne) - float(numTwo))

def multiply(numOne, numTwo):
    return str(float(numOne) * float(numTwo))

def divide(numOne, numTwo):
    try:
        return str(float(numOne) / float(numTwo))
    except ZeroDivisionError:
        return "You can't divide by zero!"

def powerOf(numOne, numTwo):
    return str(float(numOne) ** float(numTwo))


def tokenize(operations, equation, lastResult=""):
    num = lastResult
    tokens = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    for char in equation:
        if char in operations.keys():
            tokens.append(num)
            tokens.append(char)
            num = ""
        elif char in digits:
            if char == "." and "." in num:
                continue
            else:
                num += char
        else:
            continue
    tokens.append(num)
    return tokens


def evaluate():
    pass

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
    result = ""
    useLast = False

    while calcOn:
        if result:
            print("")
            print("Continue using last result?")

            useLast = input(" --> ").lower()
            if useLast in ["y", "yes", "sure", "please"]:
                useLast = True
            else:
                useLast = False

        print("")
        print("Enter your equation:")
        rawEq = input(" --> ")

        if useLast:
            cleanEq = tokenize(operations, rawEq, result)
        else:
            cleanEq = tokenize(operations, rawEq)


        print(cleanEq)

        # # Get and verify first num
        # if result:
        #     print("")
        #     print("Continue using last result?")
        #     useLast = input(" --> ").lower()

        #     if useLast in ["y", "yes", "sure", "please"]:
        #         useLast = True
        #     else:
        #         useLast = False


        # if useLast:
        #     firstNum = float(result)
        # else:
        #     validFirstNum = False
        #     while not validFirstNum:
        #         print("")
        #         print("Enter your first number:")
        #         firstNum = input(" --> ")

        #         try:
        #             firstNum = float(firstNum)
        #             validFirstNum = True
        #         except ValueError:
        #             print("")
        #             print("That's not a valid number! Try again.")


        # # Get and verify operator
        # validOperation = False
        # while not validOperation:
        #     print("")
        #     print("Enter an operation:")
        #     operator = input(" --> ")

        #     if operator in operations.keys():
        #         validOperation = True
        #     else:
        #         print("")
        #         print("That's not a valid operator! Try again.")


        # # Get and verify second num
        # validSecondNum = False
        # while not validSecondNum:
        #     print("")
        #     print("Enter your second number:")
        #     secondNum = input(" --> ")

        #     try:
        #         secondNum = float(secondNum)
        #         validSecondNum = True
        #     except ValueError:
        #         print("")
        #         print("That's not a valid number! Try again.")


        # # Do some math
        # result = operations[operator](firstNum, secondNum)

        # # Print the result
        # print("")
        # print(f"{firstNum} {operator} {secondNum} = {result}")



        print("")
        print("Would you like to perform another equation?")
        keepGoing = input(" --> ").lower()

        if keepGoing in ["no", "n", "quit", "exit"]:
            calcOn = False




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
