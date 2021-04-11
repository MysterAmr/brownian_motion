import numpy as np #importing the numpy module to use for matrix operations
import matplotlib.pyplot as plt #importing the matplotlib module to use for plotting
import random #importing the random module to use for generating pseudo-random values
#import math #importing the math module to use for basic mathematical operations

m = 16 #m will be used for the size of the ranges of for loops 
steps = [] #This list will keep track of every grid point that is visited
X = np.linspace(0, 15, m) #This line creates evenly spaced numbers on the x interval for the grid
Y = np.linspace(0, 15, m) #This line creates evenly spaced numbers on the y interval for the grid
xGrid, yGrid = np.meshgrid(X, Y) #Here we create the grid in the xy-plane. meshgrid returns 2D grid coordinates
fig, ax = plt.subplots() #subplots divides the figure into an m by n grid

def generateField(n, m): #This function generates the vector field
  vecx = [np.random.randint(-1*n,n) for i in range(m*m)] #This list stores randomly generated x-components of vectors as integers. n determines how small and large the vectors can be
  vecy = [np.random.randint(-1*n,n) for j in range(m*m)] #This list stores randomly generated y-components of vectors as integers. n determines how small and large the vectors can be
  field = [(vecx[i], vecy[i]) for i in range(m*m)] #This list stores each vecx and vecy together as actual vectors. In other words, this is vector field 
  return vecx, vecy, field #vecx, vecy, and field are returned at the end of the function

Grid = [(X[i], Y[j]) for j in range(m) for i in range(m)] #Grid stores all of the combinations of x and y grid points

def plotField(xGrid, yGrid, vecx, vecy): #This function plots the vector field
  q = ax.quiver(xGrid, yGrid, vecx, vecy) #Quiverplot displays the vectors as arrows using matplotlib
  plt.plot(xGrid, yGrid, 'ro') #Here we plot the vectors at each grid point using matplotlib

def randomWalk(steps, field): #This function will perform the actual random walk
  index = 105 #This variable is the index of the grid point I have chosen for the walker to begin at 
  count = 0 #Initializing the counter for the while loop in line 37
  currentx = Grid[index][0] #This variable is the x component of the grid point the walker is currently at
  currenty = Grid[index][1] #This variable is the y component of the grid point the walker is currently at
  steps.append((currentx, currenty)) #We append the first point to the steps list 

  while count < 10: #For every iteration of the while, a random point is generated and used to figured out the next point the walker will visit
    
    xpoint = round(random.uniform(field[index][0], currentx + field[index][0])) #This is were we calculate and round the x-component of the potential point using the x-boundary of the rectangle enclosing the vector. Remember, field is the list which contains all of the random vector lists. field[index][0] accesses the x-components of the respective vectors.
    ypoint = round(random.uniform(field[index][1], currenty + field[index][1])) #This is were we calculate and round the y-component of the potential point using the y-boundary of the rectangle enclosing the vector. Remember, field is the list which contains all of the random vector lists. field[index][1] accesses the y-components of the respective vectors
    
    #The following if-statement checks if the potential point is outside the bounds of grid. If it is, we break out of the while loop
    if xpoint < 0 or xpoint > 15:
      break
    if ypoint < 0 or ypoint > 15:
      break

    index = Grid.index((xpoint, ypoint)) #Whatever the index of the potential point is, we assign it to this variable to use in the next iteration of the while.

    currentx = xpoint #Since the potential point was in the bounds of grid, we assign its x-component to currentx
    currenty = ypoint #Since the potential point was in the bounds of grid, we assign its y-component to currenty

    steps.append((currentx, currenty)) #We append every visited point to this list
    count += 1 #Increment the counter for the while loop
  return steps #steps is returned here at the end of the function
  

def plotWalk(walk, vecx, vecy): #This function plots the random walk on the grid
  xWalk = [walk[i][0] for i in range(len(walk))] #We create a list which contains the x-components of the visited points
  yWalk = [walk[i][1] for i in range(len(walk))] #We create a list which contains the y-components of the visited points

  plotField(xGrid, yGrid, vecx, vecy) #We call the function which plots the vector field using matplotlib
  plt.title('Random walk') #We create a title for the graph
  plt.xlabel('X') #We label the x-axis
  plt.ylabel('Y') #We label the y-axis
  plt.plot(xWalk[0], yWalk[0], color='green', marker='o') #The random walker begins at the green marker
  plt.plot(xWalk, yWalk, '-') #We finally plot the actual random walk 
  plt.savefig("Random Walk") #We save the plot as "Random Walk"
  plt.show() #And now we display the plot

vecx, vecy, field = generateField(2, 16) #We assign the output of the generateField function to three variables, the x-components of the random vector, the y-components of the random vectors, and the list containing the vectors, respectively

walk = randomWalk(steps, field) #We as the output of the randomWalk vector to another variable

plotWalk(walk, vecx, vecy) #We use the above variables and use them to call the plotWalk function to finally plot the random walk and vector field
