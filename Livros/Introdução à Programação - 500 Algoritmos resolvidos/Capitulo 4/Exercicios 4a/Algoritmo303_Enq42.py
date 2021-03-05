# Program: Algoritmo303_Enq42.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/04/2020 - 11:06
# Updated:

sum_ = 0
sum_total = 0

while True:
    driver_s_license = int(input("Enter with driver's license number: "))
    if driver_s_license == 0:
        break
    elif driver_s_license >= 1 and driver_s_license <= 4327:
        number_fines = int(input("Enter with number of fines: "))
        sum_ = 0
        for e in range(number_fines):
            value = float(input("Enter with the value of %d° fine:  " %(e+1)))
            sum_+=value
        print(sum_)
    else:
        print("Invalid Option!")
    sum_total+=sum_
print(sum_total)       
        
        
