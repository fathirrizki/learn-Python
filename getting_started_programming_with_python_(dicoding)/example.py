def add(a,b):
    result = a + b
    return result

def sub(a,b):
    result = a - b
    return result

def mul(a,b):
    result = a * b
    return result

def div(a,b):
    result = a / b
    return result

def maks(*args):
    comparator = args[0]
    for a in range(1, len(args)):
        if comparator < args[a]:
            comparator = args[a]
    return comparator

def mins(*args):
    comparator = args[0]
    for a in range(1, len(args)):
        if comparator > args[a]:
            comparator = args[a]
    return comparator