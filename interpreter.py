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