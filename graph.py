import turtle

# Adjusted sample data points with spread-out x-values
data_points = [(1, 2), (7, 3), (12, 2.75)]

# Calculate the sums and other necessary values for the formula
n = len(data_points)
sum_x = sum([x for x, y in data_points])
sum_y = sum([y for x, y in data_points])
sum_xy = sum([x * y for x, y in data_points])
sum_x_squared = sum([x ** 2 for x, y in data_points])

# Calculate the slope (m) and y-intercept (b) for the best-fit line
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = (sum_y - m * sum_x) / n

# Create a turtle object
graph = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.title("Best-Fit Line Graph")

# Function to set up a scaled coordinate system
def setup_coordinates():
    graph.speed(0)  # Set the fastest speed for drawing
    graph.penup()
    graph.goto(-150, -150)  # Move to the bottom-left corner of the graph
    graph.pendown()
    graph.forward(300)  # Draw the x-axis
    graph.backward(300)
    graph.left(90)
    graph.forward(300)  # Draw the y-axis
    graph.backward(300)
    graph.right(90)

# Function to plot the best-fit line
def plot_best_fit_line(m, b):
    graph.penup()
    graph.goto(1, m * 1 + b)  # Start point based on data
    graph.pendown()
    graph.goto(12, m * 12 + b)  # End point based on data

# Plot the axes
setup_coordinates()

# Plot the best-fit line
plot_best_fit_line(m, b)

# Plot the data points
graph.penup()
for x, y in data_points:
    scaled_x = x * 20  # Scaling up the x-values for better visibility
    scaled_y = y * 20  # Scaling up the y-values for better visibility
    graph.goto(scaled_x, scaled_y)
    graph.dot(10)  # Dot size for the data points

# Hide the turtle cursor
graph.hideturtle()

# Close the window when clicked
screen.exitonclick()
