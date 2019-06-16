def parse(s):
    curContainer = []
    valueStart = -1
    item = None
    itemComplete = False
    stack = []
    for i in xrange(0, len(s)):
        if s[i] == ' ':
            continue

        if s[i] == '[':
            stack.append(curContainer)
            curContainer = []
            item = None
            itemComplete = False
            valueStart = -1
        elif s[i] == ']':
            if itemComplete:
                curContainer.append(item)
            item = curContainer
            itemComplete = True
            curContainer = stack.pop()
        elif s[i] == ',':
            if itemComplete:
                curContainer.append(item)
                item = None
            else:
                raise Exception, "invalid format"
        elif s[i] in '1234567890':
            if valueStart == -1:
                valueStart = i
            if i + 1 == len(s) or s[i + 1] in '[], ':
                item = int(s[valueStart: i + 1])
                itemComplete = True
                valueStart = -1
        else:
            print s[i]
            raise Exception, "invalid character"

        if i + 1 == len(s):
            if itemComplete:
                curContainer.append(item)
                item = None
                itemComplete = False
            else:
                raise Exception, "invalid format"

    return curContainer[0]


if __name__ == "__main__":
    print(parse('[123, 4, [5, 6], [9, [10, [11], [] ]]]'))