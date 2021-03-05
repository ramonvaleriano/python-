# Program: Algoritmo323_Enq61.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/04/2020 - 18:54
# Updated:

maximum = 2000
cont = 1
member = 0
non_member = 0
tax_member = 10
tax_non_member = 20
result_n = 0
result_m = 0
sum_m = 0
sum_n = 0


while cont<maximum:
    quantity = int(input("Enter with quantity of tickets: "))
    if quantity == -999:
        break
    elif quantity>0:
        option = input("Enter with the option:\nM - Member or N - Non-member -- >: ")
        option = option.upper()
        if option == "M" or option == "N":
            if option == "M":
                member+=quantity
                result_m = quantity * tax_member
                sum_m+=result_m
                cont+=quantity
                print(result_m)
            elif option == "N":
                non_member+=quantity
                result_n = quantity * tax_non_member
                sum_n+=result_n
                print(result_n)
                cont+=quantity
            total = sum_m + sum_n
        else:
            print("Invalid Option!")
    else:
        print("Invalid Option!")
        
conversion = (cont*member)/100
print()
print(member)
print(non_member)
print(conversion)
print(sum_m)
print(sum_n)
print(total)
