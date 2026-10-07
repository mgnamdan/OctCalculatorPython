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
            if not num:
                return []
            else:
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


def evaluate(operations, tokensIn):
    tokens = tokensIn
    for operator in operations.keys():
        newTokens = [tokens[0]]
        for idx in range(1, len(tokens), 2):
            op = tokens[idx]
            right = tokens[idx+1]
            if op == operator:
                left = newTokens.pop()
                result = operations[op](left, right)
                newTokens.append(result)
            else:
                newTokens.append(op)
                newTokens.append(right)
        tokens = newTokens
    return tokens.pop()


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
        validEqIn = False
        while not validEqIn:
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
                if rawEq[0] in operations.keys():
                    cleanEq = tokenize(operations, rawEq, result)
                    if len(cleanEq) == 0:
                        print("")
                        print("Equation in an unrecognized form. Try again.")
                    else:
                        validEqIn = True
                else:
                    print("")
                    print("Equation in an unrecognized form. Try again.")
            else:
                if rawEq[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                    cleanEq = tokenize(operations, rawEq)
                    if len(cleanEq) == 0:
                        print("")
                        print("Equation in an unrecognized form. Try again.")
                    else:
                        validEqIn = True
                else:
                    print("")
                    print("Equation in an unrecognized form. Try again.")

        result = evaluate(operations, cleanEq)

        if useLast:
            print(f"{result} {rawEq} = {result}")
        else:
            print(f"{rawEq} = {result}")

        print("")
        print("Would you like to perform another equation?")
        keepGoing = input(" --> ").lower()

        if keepGoing in ["no", "n", "quit", "exit"]:
            calcOn = False




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
