# Program: desafio_032.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:41

anos_bisestos = list()
anos_bisestos = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]

ano_atual = int(input('Digite o ano atual: '))
if ano_atual in anos_bisestos:
    print('É um ano bissesto')
else:
    print('Não é ano bissesto')