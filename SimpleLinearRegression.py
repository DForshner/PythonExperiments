import matplotlib.pyplot as plot

# Constants 
X = 0
Y = 1

def linear_regression(points):
    sumxy = 0.0
    sumx = 0.0
    sumy = 0.0
    sumxx = 0.0
 
    # Determine slope of line that minimizes error 
    # Slope = ( Sum(xy) - Sum(x)Sum(y)/points ) / ( Sum(x^2) - (Sum(x))^2)
    for point in points:
        assert len(point) is 2
        sumxy += point[X] * point[Y]
        sumx += point[X]
        sumy += point[Y]
        sumxx += point[X]**2

    n = len(points)
    slope = (sumxy - ((sumx * sumy) / n) ) / ( sumxx - (sumx**2 / n) )

    # Determine the x axis crossing point
    initial = (sumy - (slope * sumx)) / n

    # Get points for line that best fits the data
    LinearRegression = []
    for point in points:
        LinearRegression.append([point[X], initial + (slope * point[X])])

    return LinearRegression

def plot_line(line):
    x = []
    y = []

    for i in range(len(line)):
        x.append(line[i][X])
        y.append(line[i][Y])
    plot.plot(x, y, 'b', linewidth=2)


def plot_points(points):
    x = []
    y = []
    
    for i in range(len(points)):
        x.append(points[i][X])
        y.append(points[i][Y])

    plot.plot(x, y,'ro')


''' ___MAIN___ '''
points = [ [0, 1], [1, 2], [2, 3], 
    [5, 4], [6, 3], [6, 5], [8, 6], 
    [10, 10], [11, 10], [12, 14] ]

line = linear_regression(points)

plot_points(points)
plot_line(line)
plot.title('Linear Regression')
plot.show()