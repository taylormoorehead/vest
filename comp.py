# import csv
# filename = "file.txt"
# with open(filename, 'w') as file:
#     pass
# csvpath = "data.csv"
# with open(csvpath, mode="r") as file:
#     reader = csv.reader(file)
#     headers = next(reader)
#     for row in reader:
#         equity, debt, erate, drate, tax = row
#         company_wacc = (equity / (debt + equity)) * erate + (debt / (debt + equity)) * drate * (1 - tax)
#         with open(filename, 'w') as file:
#             file.write(company_wacc + "\n")

import turtle

filename = "comp-file.txt"
company_wacc = (1 / (1 + 1)) * 1 + (1 / (1 + 1)) * 1 * (1 - 0.5)
with open(filename, 'w') as file:
    file.write(str(company_wacc) + "\n")

graph = turtle.Turtle()
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
graph.penup()
graph.hideturtle()
screen = turtle.Screen()
screen.title("Graph")
screen.exitonclick()