
#don't like external libraries but have to use for large factorials, trig, and log
import math

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
            length = 1
            decimal = 0
            temp = int(input[num])
            while (len(input) > num + n) and (input[num + n].isnumeric() or (input[num + n] == " ") or (input[num + n] == ".") or (input[num + n] == ",")):
                if (input[num + n] == " ") or (input[num + n] == ","):
                    n = n + 1
                    continue
                elif input[num + n] == ".":
                    decimal = length
                    n = n + 1
                    continue
                elif input[num + n].isnumeric():
                    temp = temp * 10 + int(input[num + n])
                    n = n + 1
                    length = length + 1
                    continue
            if decimal == 0:
                decimal = length
            skip = n - 1
            temp = temp / (10 ** (length - decimal))
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

def reformat(input):
    #reformat expression to be in a form that can be used by the calculator
    if input.count(")") != input.count("("):
        print("Invalid input")
        exit()
    output = []
    skip = 0
    isdone = False
    while isdone == False:
        isdone = True
        for num in range(len(input)):
            if input[num] == "(":
                isdone = False
                n = 0
                open_parentheses = 0
                if skip > 0:
                    skip = skip - 1
                    continue
                while True:
                    n = n + 1
                    if num + n == len(input):
                        print("Invalid input")
                        exit()
                    if input[num + n] == "(":
                        open_parentheses = open_parentheses + 1
                    if input[num + n] == ")":
                        if open_parentheses > 0:
                            open_parentheses = open_parentheses - 1
                        else:
                            break
                temp = []
                temp.extend(input[0:num])
                p_block = input[num + 1:num + n]
                p_block = reformat(p_block)
                temp.append(p_block)
                temp.extend(input[num + n + 1:len(input)])
                input = temp
                skip = n
                break
    output = input
    return output

def calculate(expression, value):
    #calculate the value of the expression
    output = expression
    while len(output) > 1:
        print(output)
        skip = False
        for num in range(len(output)):
            print("iter " + str(num) + " val= " + str(output[num]))
            if type(output[num]) == list:
                output[num] = calculate(output[num], value)
                skip = True
                break
            elif output[num] == "x":
                output[num] = value
                skip = True
                break
            elif output[num] == "e":
                output[num] = 2.718281828459045
                skip = True
                break
            elif output[num] == "pi":
                output[num] = 3.141592653589793
                skip = True
                break
        if skip == True:
            continue
        for num in range(len(output)):
            if output[num] == "sin":
                output[num + 1] = math.sin(output[num + 1])
                del output[num]
                skip = True
                break
            elif output[num] == "cos":
                output[num + 1] = math.cos(output[num + 1])
                del output[num]
                skip = True
                break
            elif output[num] == "tan":
                output[num + 1] = math.tan(output[num + 1])
                del output[num]
                skip = True
                break
            elif output[num] == "sec":
                output[num + 1] = 1 / math.cos(output[num + 1])
                del output[num]
                skip = True
                break
            elif output[num] == "csc":
                output[num + 1] = 1 / math.sin(output[num + 1])
                del output[num]
                skip = True
                break
            elif output[num] == "cot":
                output[num + 1] = 1 / math.tan(output[num + 1])
                del output[num]
                skip = True
                break
        if skip == True:
            continue
        for num in range(len(output)):
            if output[num] == "^":
                output[num - 1] = output[num - 1] ** output[num + 1]
                del output[num]
                del output[num]
                skip = True
                break
            elif output[num] == "sqrt":
                output[num + 1] = output[num + 1] ** 0.5
                del output[num]
                skip = True
                break
            elif output[num] == "ln":
                output[num + 1] = math.log(output[num + 1])
                del output[num]
                skip = True
                break
            elif output[num] == "log":
                output[num + 1] = math.log(output[num + 1], 10)
                del output[num]
                skip = True
                break
        if skip == True:
            continue
        for num in range(len(output)):
            if output[num] == "*":
                output[num - 1] = output[num - 1] * output[num + 1]
                del output[num]
                del output[num]
                skip = True
                break
            elif output[num] == "/":
                output[num - 1] = output[num - 1] / output[num + 1]
                del output[num]
                del output[num]
                skip = True
                break
            elif isinstance(output[num], (int, float)):
                try:
                    if isinstance(output[num + 1], (int, float)):
                        output[num] = output[num] * output[num + 1]
                        del output[num + 1]
                        skip = True
                        break
                except:
                    break
        if skip == True:
            continue
        print("late" + str(output))
        for num in range(len(output)):
            if output[num] == "+":
                output[num - 1] = output[num - 1] + output[num + 1]
                del output[num]
                del output[num]
                skip = True
                break
            elif output[num] == "-":
                output[num - 1] = output[num - 1] - output[num + 1]
                del output[num]
                del output[num]
                skip = True
                break
        if skip == True:
            continue

    return output[0]

def derivative(input):
    # calculate derivative of input array
    output = input
    return output

def factorial(value):
    if value > 20:
        # only use this for large numbers for speed since I am trying to avoid using any external libraries
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

def main():
    # read input
    print("Careful about PEMDAS and please avoid confusing variable usage")
    user_input = input("Enter a function using standard math symbols: ")
    expression = read_input(user_input)
    print(expression)
    expression = reformat(expression)
    print(expression)
    a = input("Enter value: ")
    print(calculate(expression, int(a)))
    #a = input("Enter where to center series: ")
    #n = input("Enter number of iterations: ")
    #result = taylor_series(expression, a, n)
    #print(result)
    return

if __name__ == '__main__':
    main()