def calculate(self, s):
    # Write your code here
    numStart = -1
    opStack, numStack = [], []
    funcMap = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    s += '#'
    for i in range(len(s)):
        if s[i].isdigit() and (i == 0 or not s[i - 1].isdigit()):
            numStart = i
        if s[i].isdigit() and (i + 1 == len(s) or not s[i + 1].isdigit()):
            numStack.append(int(s[numStart: i + 1]))

        if s[i] in '+-*/()#':
            while len(opStack) > 0 and opStack[-1] != '(' and (s[i] in '+-)#' or opStack[-1] in '*/'):
                b = numStack.pop()
                a = numStack.pop()
                numStack.append(funcMap[opStack.pop()](a, b))
            if s[i] == ')':
                opStack.pop()
            else:
                opStack.append(s[i])

    return numStack[-1]

#print (calculate(0, "2*(5+5*2)/3+(6/2+8)"))


with open('/Users/heiyanbin/Downloads/output000.txt') as f:
    while True:
        print(f.readline())