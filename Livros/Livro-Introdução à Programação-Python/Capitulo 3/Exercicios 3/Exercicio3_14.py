# Program: Exercicio3_14.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 14/03/2020 - 13:30 
# Updated:

quantity = int(input("Enter with the quantity of cigarettes: "))
years = int(input("Enter with the quantity of years: "))

accumulated_cigarettes = quantity*10 #Total em minutos de quantos cigarros por dia
conversionDay_minute = 24*60 #Conversão de 1 dia para minutos
#accumulated_years = years*conversionDay_minute #Conversão de anos fumados para minutos

calculation_minutes = years*accumulated_cigarettes
calculation_conversion = calculation_minutes/conversionDay_minute
# calculation_conversion = int(calculation_conversion)


print("The quantity of days is %5.2f" % calculation_conversion)

