

def read_input(input):
    input.split()
    output = []
    skip = 0
    variable = ""
    for num in range(len(input)):
        if skip > 0:
            skip = skip - 1
            continue
        char = input[num]
        charused = False
        if char == " ":
            continue
        elif char == "+":
            output.append("+")
        elif char == "-":
            output.append("-")
        elif char == "*":
            output.append("*")
        elif char == "/":
            output.append("/")
        elif char == "^":
            output.append("^")
        elif (char == "(") or (char == "[") or (char == "{"):
            output.append("(")
        elif (char == ")") or (char == "]") or (char == "}"):
            output.append(")")
        elif char == ".":
            n = 1
            temp = 0
            while input[num + n].isnumeric() or (input[num + n] == " "):
                if input[num + n] == " ":
                    n = n + 1
                    continue
                temp = temp + (input[num + n] * (10 ** (-n)))
                n = n + 1
            skip = n - 1
            output.append(temp)
        elif char.isnumeric():
            n = 1
            decimal = 1
            temp = int(input[num])
            while (len(input) > num + n) and (input[num + n].isnumeric() or (input[num + n] == " ") or (input[num + n] == ".") or (input[num + n] == ",")):
                if (input[num + n] == " ") or (input[num + n] == ","):
                    n = n + 1
                    continue
                elif input[num + n] == ".":
                    decimal = n
                    n = n + 1
                    continue
                temp = temp + (int(input[num + n]) * (10 ** (n)))
                n = n + 1
            skip = n - 1
            temp = temp / (10 ** (n - decimal))
            output.append(temp)
        elif char == "s": #sin, sec, sqrt
            if (input[num + 1] == "i") and (input[num + 2] == "n"):
                output.append("sin")
                skip = 2
                charused = True
            elif (input[num + 1] == "e") and (input[num + 2] == "c"):
                output.append("sec")
                skip = 2
                charused = True
            elif (input[num + 1] == "q") and (input[num + 2] == "r") and (input[num + 3] == "t"):
                output.append("sqrt")
                skip = 3
                charused = True
        elif char == "c": #cos, csc, cot
            if (input[num + 1] == "o") and (input[num + 2] == "s"):
                output.append("cos")
                skip = 2
                charused = True
            elif (input[num + 1] == "s") and (input[num + 2] == "c"):
                output.append("csc")
                skip = 2
                charused = True
            elif (input[num + 1] == "o") and (input[num + 2] == "t"):
                output.append("cot")
                skip = 2
                charused = True
        elif char == "t": #tan
            if (input[num + 1] == "a") and (input[num + 2] == "n"):
                output.append("tan")
                skip = 2
                charused = True
        elif char == "l": #ln, log
            if (input[num + 1] == "n"):
                output.append("ln")
                skip = 1
                charused = True
            elif (input[num + 1] == "o") and (input[num + 2] == "g"):
                output.append("log")
                skip = 2
                charused = True
        elif (char == "e") and (not input[num + 1].isalpha()): #e
            output.append("e")
            charused = True
        elif char == "p": #pi
            if (input[num + 1] == "i"):
                output.append("pi")
                skip = 1
                charused = True
        if char.isalpha() and (charused == False):
            if variable == char:
                output.append(char)
            elif variable == "":
                variable = char
                output.append(char)
            else:
                print("Invalid input")
                exit()
    return output

def calculate(expression, value):
    output = input
    return output

def derivative(input):
    # calculate derivative of input array
    output = input
    return output

def factorial(value):

    if value > 20:
        # only use this for large numbers for speed since I am trying to avoid using any external libraries
        import math
        return math.factorial(value)
    output = 1
    while value > 0:
        output = output * value
        value = value - 1
    return output

def taylor_series(input, a, n):
    # calculate taylor series of input array
    output = input
    return output

def test_if_valid(input):
    # test if expression inputted is valid (no extra symbols, etc.)
    bool = True
    return bool

def main():
    # read input
    print("Careful about PEMDAS and please avoid confusing variable usage")
    user_input = input("Enter a function using standard math symbols: ")
    expression = read_input(user_input)
    print(expression)
    '''test_if_valid(expression)
    a = input("Enter where to center series: ")
    n = input("Enter number of iterations: ")
    result = taylor_series(expression, a, n)
    print(result)'''
    return

if __name__ == '__main__':
    main()