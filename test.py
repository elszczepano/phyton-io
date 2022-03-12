# Simple calc advanced

def hello(name):
    return "Hemlo" + str(name)

def add(a,b):
    sum = float(a) + float(b)
    return sum;

def sub(a,b):
    diff = float(a) - float(b)
    return diff;

first = input()
second = input()

print(add(first,second))
