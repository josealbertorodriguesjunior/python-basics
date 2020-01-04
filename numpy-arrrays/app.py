# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]

# exercise
# using numpy to convert kg in lbs
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# creating a numpy array
np_weight_kg = np.array(weight_kg)

# creating a new variable to store the values of kg converted to lbs
np_weight_lbs = np_weight_kg * 2.2

# printing the value in lbs
print("Value in LBS: ",np_weight_lbs)