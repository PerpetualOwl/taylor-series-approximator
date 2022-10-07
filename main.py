
#don't like external libraries but have to use for large factorials, trig, and log
import math
from tkinter import N

def clearvars():
    for variable in dir():
        if variable[0:2] != "__":
            del globals()[variable]

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
    isdone = False
    while isdone == False:
        isdone = True
        for num in range(len(output)):
            if input[num] == "-":
                input[num] = "+"
                input.insert(num + 1, -1)
                isdone = False
                continue
    return output

def calculate(expression, value):
    #calculate the value of the expression
    out_list = []
    out_list = expression
    for num in range(len(out_list)):
        if out_list[num] == "x":
            out_list[num] = value
    while len(out_list) > 1:
        skip = False
        for num in range(len(out_list)):
            if type(out_list[num]) == list:
                out_list[num] = calculate(out_list[num], value)
                skip = True
                break
            elif out_list[num] == "x":
                out_list[num] = value
                skip = True
                break
            elif out_list[num] == "e":
                out_list[num] = 2.718281828459045
                skip = True
                break
            elif out_list[num] == "pi":
                out_list[num] = 3.141592653589793
                skip = True
                break
        if skip == True:
            continue
        for num in range(len(out_list)):
            if out_list[num] == "sin":
                out_list[num + 1] = math.sin(out_list[num + 1])
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "cos":
                out_list[num + 1] = math.cos(out_list[num + 1])
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "tan":
                out_list[num + 1] = math.tan(out_list[num + 1])
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "sec":
                out_list[num + 1] = 1 / math.cos(out_list[num + 1])
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "csc":
                out_list[num + 1] = 1 / math.sin(out_list[num + 1])
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "cot":
                out_list[num + 1] = 1 / math.tan(out_list[num + 1])
                del out_list[num]
                skip = True
                break
        if skip == True:
            continue
        for num in range(len(out_list)):
            if out_list[num] == "^":
                out_list[num - 1] = out_list[num - 1] ** out_list[num + 1]
                del out_list[num]
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "sqrt":
                out_list[num + 1] = out_list[num + 1] ** 0.5
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "ln":
                out_list[num + 1] = math.log(out_list[num + 1])
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "log":
                out_list[num + 1] = math.log(out_list[num + 1], 10)
                del out_list[num]
                skip = True
                break
        if skip == True:
            continue
        for num in range(len(out_list)):
            if out_list[num] == "*":
                out_list[num - 1] = out_list[num - 1] * out_list[num + 1]
                del out_list[num]
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "/":
                out_list[num - 1] = out_list[num - 1] / out_list[num + 1]
                del out_list[num]
                del out_list[num]
                skip = True
                break
            elif isinstance(out_list[num], (int, float)):
                try:
                    if isinstance(out_list[num + 1], (int, float)):
                        out_list[num] = out_list[num] * out_list[num + 1]
                        del out_list[num + 1]
                        skip = True
                        break
                except:
                    break
        if skip == True:
            continue
        for num in range(len(out_list)):
            if out_list[num] == "+":
                out_list[num - 1] = out_list[num - 1] + out_list[num + 1]
                del out_list[num]
                del out_list[num]
                skip = True
                break
            elif out_list[num] == "-":
                out_list[num - 1] = out_list[num - 1] - out_list[num + 1]
                del out_list[num]
                del out_list[num]
                skip = True
                break
        if skip == True:
            continue
    if len(out_list) == 1:
        return out_list[0]
    else:
        print("Invalid input")
        exit()

def derivative(input):
    # calculate derivative of input array
    list_of_additions = []
    for i in range(len(input)):
        if input[i] == "+":
            list_of_additions.append[i]
    if len(list_of_additions) > 0: 
        prev = 0
        for j in list_of_additions:
            temp = derivative(input[prev:j])
            del input[prev:j]
            input.insert(prev, temp)
            prev = j + 1
    output = input
    return output

def derivative_at_value(input, value):
    # calculate derivative of input array at value
    value = float(value)
    h = 1
    amount = 0
    prev = 123456789
    while amount < 7:
        input1 = input.copy()
        input2 = input.copy()
        j = (calculate(input1, value + h) - calculate(input2, value)) / h
        if prev - j < .0001:
            amount = amount + 1
        else:
            amount = 0
        prev = j
        h = h / 10
    return round(j, 5)

def nth_derivative_at_value(input, value, n):
    # calculate nth derivative of input array at a specific value
    value = float(value)
    n = int(n)
    dx = 1
    amount = 0
    prev = 123456789
    while amount < 7:
        total = 0
        for k in range(n + 1):
            temp = (-1) ** k
            temp = temp * factorial(n) / factorial(k) / factorial(n - k)
            input1 = input.copy()
            temp = temp * calculate(input1, (value + dx * (n - k)))
            temp = temp / (dx ** n)
            total = total + temp
        print(prev-total)
        if prev - total < .0001:
            amount = amount + 1
        else:
            amount = 0
        prev = total
        dx = dx / 10
    return round(total, 5)

def factorial(value):
    if value > 100:
        # only use this for large numbers for speed since I am trying to avoid using any external libraries
        # however, math.factorial is fast since it is a C implementation
        return math.factorial(int(value))
    output = 1
    while value > 0:
        output = output * value
        value = value - 1
    return output

def taylor_series(input, a, n):
    # calculate taylor series of input array
    output = input
    return output

def x(input):
    output = input
    return output

def main():
    # read input
    print("Careful about PEMDAS and please avoid confusing variable usage")
    user_input = input("Enter a function using standard math symbols: ")
    exp = read_input(user_input)
    exp = reformat(exp)
    a = input("Enter value: ")
    dvin = exp.copy()
    print(nth_derivative_at_value(dvin, a, 5))
    dvin2 = exp.copy()
    print(nth_derivative_at_value(dvin2, a, 30))
    
    #a = int(input("Enter where to center series: "))
    #n = int(input("Enter number of iterations: "))
    #result = taylor_series(expression, a, n)
    #print(result)
    return

if __name__ == '__main__':
    main()