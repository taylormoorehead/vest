import sys
import turtle
import csv

path = sys.argv[1]

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

program = {}
code = []
token = 0
#label = {}
comments = []

for line in lines:
    parts = line.split(" ")
    operation = parts[0]

    if operation == "":
        continue

    # if operation.endswith(":"):
    #     label[operation[:-1]] = token
    #     continue

    # program.append(operation)
    # token += 1

    code.append(operation)
    token += 1

    if operation == "write":
        filename = parts[3]
        program["filename"] = filename
        token += 1

    if operation == "wacc":
        e = float(parts[3].split(",")[0])
        d = float(parts[4].split(",")[0])
        re = float(parts[5].split(",")[0])
        rd = float(parts[6].split(",")[0])
        t = float(parts[7].split(")")[0])
        program["e"] = e
        program["d"] = d
        program["re"] = re
        program["rd"] = rd
        program["t"] = t
        token += 1
    
    if operation == "graph":
        graphname = parts[1]
        program["graphname"] = graphname
        token += 1

    if operation.__contains__("//"):
        comments.append(operation)


def setup_coordinates():
    graph.speed(0)
    graph.penup()
    graph.goto(-150, -150)
    graph.pendown()
    graph.forward(300)
    graph.backward(300)
    graph.left(90)
    graph.forward(300)
    graph.backward(300)
    graph.right(90)

data_points = [(1, 2), (7, 3), (12, 2.75)]

count = 0
while code[count] != "END":
    operation = code[count]
    count += 1

    if operation == "write":
        with open(program.get("filename"), "w") as file:
            file.write(str(program.get("wacc")))
            file.write("\n")
    
    elif operation == "wacc":
        e = program.get("e")
        d = program.get("d")
        re = program.get("re")
        rd = program.get("rd")
        t = program.get("t")
        wacc = (e / (d + e)) * re + (d / (d + e)) * rd * (1 - t)
        program["wacc"] = wacc
    
    elif operation == "graph":
        graph = turtle.Turtle()
        setup_coordinates()
        graph.penup()

        for x, y in data_points:
            scaled_x = x - 150
            scaled_y = y - 150
            graph.goto(scaled_x, scaled_y)
            graph.dot(2.5)

        graph.hideturtle()
        screen = turtle.Screen()
        screen.title(program.get("graphname"))
        screen.exitonclick()
    
    elif comments.__contains__(operation):
        continue

print("Program finished.")