import turtle

data_points = [(1, 2), (7, 3), (12, 2.75)]

n = len(data_points)
sum_x = sum([x for x, y in data_points])
sum_y = sum([y for x, y in data_points])
sum_xy = sum([x * y for x, y in data_points])
sum_x_squared = sum([x ** 2 for x, y in data_points])

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print(m, b)

graph = turtle.Turtle()

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

def plot_best_fit_line(m, b):
    graph.penup()
    graph.goto(1, m * 1 + b)
    graph.pendown()
    graph.goto(12, m * 12 + b)

setup_coordinates()

# plot_best_fit_line(m, b)

graph.penup()
for x, y in data_points:
    scaled_x = x - 150
    scaled_y = y - 150
    graph.goto(scaled_x, scaled_y)
    graph.dot(2.5)

graph.goto(-150, -150)
graph.pendown()
graph.goto(-150 + 12, -150 + 2.964)

graph.hideturtle()

screen = turtle.Screen()
screen.title("Best-Fit Line Graph")

screen.exitonclick()
