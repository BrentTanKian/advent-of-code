# Dictionary to store data
# For each reindeer, store speed, travel time, rest time, current time travelled, current distance travelled, current cycle, cycle travel time, cycle total time, points
# For each reindeer determine the current cycle, cycle travel time and cycle total time
# After each second, if current time travelled < cycle travel time, increment distance and time travelled
# Else if current time >= cycle travel time but < cycle total time, only increment time travelled
# Else if current time > cycle travel time and equals to cycle total time, increment cycle and determine new cycle travel time and new cycle total time again
# Also determine max distance after each second and allocate points