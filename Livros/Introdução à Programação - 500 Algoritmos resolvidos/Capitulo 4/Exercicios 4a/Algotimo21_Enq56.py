# Program: Algotimo21_Enq56.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 08/04/2020 - 11:44
# Updated:

total_commission_sale= 0
total_comission_personal = 0
total_profit = 0

while True:
    sale_price = float(input("Enter with the sale price: "))
    commission_sale = (sale_price*50)/100 
    comission_personal = (sale_price*3)/100 
    profit = sale_price - commission_sale - comission_personal
    total_commission_sale+=commission_sale
    total_comission_personal+=comission_personal
    total_profit+=profit
    print(commission_sale) 
    print(comission_personal) 
    print(profit = sale_price)
    print()
print(total_commission_sale)
print(total_comission_personal)
print(total_profit)
