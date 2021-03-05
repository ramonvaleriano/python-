# Program: Algoritmo308_Enq47.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 08:58
# Updated:

distance_total = 0
liters_total = 0
time_total = 0

while True:
    velocity = float(input("Enter whith the car velocity: "))
    if velocity < 0:
        break
    time = float(input("Enter with the time of the travel: "))
    distance = time*velocity
    liters = distance/10
    print(distance)
    print(liters)
    distance_total+=distance
    liters_total+=liters
    time_total+=time
    print()
print()
print(distance_total)
print(liters_total)
print(time_total)
