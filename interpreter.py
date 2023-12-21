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

    if operation == "":

        program.append()
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

while program[count] != "HALT":
    operation = program[count]
    count += 1