import sys

path = sys.argv[1]

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

program = []
token = 0
label = {}
for line in lines:
    parts = line.split(" ")
    operation = parts[0]

    if operation == "":
        continue

    if operation.endswith(":"):
        label[operation[:-1]] = token
        continue

    program.append(operation)
    token += 1

    if operation == "create":
        filename = ' '.join(parts[1:])[1:-1]
        program.append(filename)
        token += 1
    
    


class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number

    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number

    def top(self):
        return self.buf[self.sp]

count = 0
stack = Stack(256)

while program[count] != "END":
    operation = program[count]
    count += 1

    if operation == "write":
        count += 2
        filename = program[count]
        with open(filename, "w") as file:
            file.write(stack.pop())
            file.write("\n")
        count += 1
    
    elif program[count + 1].split("(")[0] == "wacc":
        e = float(program[count + 1].split("(")[1].split(", ")[0])
        d = float(program[count + 1].split("(")[1].split(", ")[1])
        re = float(program[count + 1].split("(")[1].split(", ")[2])
        rd = float(program[count + 1].split("(")[1].split(", ")[3])
        t = float(program[count + 1].split("(")[1].split(", ")[4].split(")")[0])
        wacc = (e / (d + e)) * re + (d / (d + e)) * rd * (1 - t)
        stack.push(wacc)
        count += 2
    
    elif operation == "for":
        
    
