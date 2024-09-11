# Author "Conor"
# Date Sept 2024
# Title "Task 6"

# Constants
PI = 3.14

# Variables for the cylinder's dimensions
height = 10
radius = 2

# Calculate the volume of the cylinder
volume = PI * (radius ** 2) * height

# Assign a large value to totalLiquid
toalLiquid = 5000

#Calculate the number of cylinders needed
number_of_cylinders = totalLiquid / volume

# Print out the results
print(f"Volume of the cylinder: {volume}")
print(f"Total liquid to be carried: {totalLiquid}")
print(f"Number of cylinders needed: {number_of_cylinders}")