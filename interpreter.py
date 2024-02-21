import sys
import turtle
import csv

path = sys.argv[1]

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

program = {}
code = []
comments = []
parts = []

for line in lines:
    parts = line.split(" ")
    operation = parts[0]

    if operation == "" or operation.__contains__("//"):
        continue

    # if operation.endswith(":"):
    #     label[operation[:-1]] = token
    #     continue

    program[operation] = line
    # token += 1

    code.append(operation)

    if operation == "write":
        i = 2
        while i < parts.__len__():
            while not parts[i].__contains__("//"):
                graphname = parts[i]
                program["graphname"] = graphname
                break
            i += 1
        filename = parts[i - 1]
        program["filename"] = filename

    if operation == "wacc":
        e = float(parts[3].split(",")[0])
        d = float(parts[4].split(",")[0])
        re = float(parts[5].split(",")[0])
        rd = float(parts[6].split(",")[0])
        t = float(parts[7].split(")")[0])
        program["equity"] = e
        program["debt"] = d
        program["equityrate"] = re
        program["debtrate"] = rd
        program["tax"] = t
    
    if operation == "future_value":
        pv = float(parts[3].split(",")[0])
        r = float(parts[4].split(",")[0])
        n = float(parts[5].split(",")[0])
        var = parts[1]
        program["presentvalue"] = pv
        program["rate"] = r
        program["time"] = n
        program[var] = var
    
    if operation == "graph":
        for i in range(parts.__len__()):
            while not parts[i].__contains__("//"):
                graphname = parts[i]
                program["graphname"] = graphname
                break

    if operation.__contains__("//"):
        comments.append(operation)

vis_graph = False

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
    vis_graph = True

data_points = []
index = 0

with open(graphname, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # print(row[0], row[1])
        data_points.append(())
        data_points[index] = (float(row[0]), float(row[1]))
        index += 1

n = len(data_points)
sum_x = sum([x for x, y in data_points])
sum_y = sum([y for x, y in data_points])
sum_xy = sum([x * y for x, y in data_points])
sum_x_squared = sum([x ** 2 for x, y in data_points])

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = (sum_y - m * sum_x) / n

count = 0
while code[count] != "END":
    operation = code[count]
    count += 1

    if operation == "write":
        with open(program.get("filename"), "w") as file:
            file.write(str(program["wacc"]))
            file.write("\n")
    
    elif operation == "wacc":
        e = program.get("equity")
        d = program.get("debt")
        re = program.get("equityrate")
        rd = program.get("debtrate")
        t = program.get("tax")
        wacc = (e / (d + e)) * re + (d / (d + e)) * rd * (1 - t)
        program["wacc"] = wacc
    
    elif operation == "future_value":
        pv = program.get("presentvalue")
        r = program.get("rate")
        n = program.get("time")
        future_value = pv * (1 + r) ** n
        program[var] = future_value
    
    elif operation == "graph":
        graph = turtle.Turtle()
        if not vis_graph: setup_coordinates()
        graph.penup()

        for x, y in data_points:
            scaled_x = x - 150
            scaled_y = y - 150
            graph.goto(scaled_x, scaled_y)
            graph.dot(2.5)
        
        line_end = m * 12 + b
        print(line_end)
        
        graph.goto(-150, -150)
        graph.pendown()
        graph.goto(-150 + 12, -150 + line_end)

        graph.hideturtle()
        screen = turtle.Screen()
        screen.title(program.get("graphname"))
        turtle.penup()
        graph.hideturtle()
        turtle.goto(0, 200)
        graph.hideturtle()
        turtle.write(program.get("graphname"), font=("Arial", 24, "normal"), align="center")
        graph.hideturtle()
        turtle.done()
    
    elif comments.__contains__(operation):
        continue

print("Program finished.")