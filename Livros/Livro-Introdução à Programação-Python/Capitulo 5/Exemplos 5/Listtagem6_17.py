# Program: Listtagem6_17.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 08:37
# Updated:

l = ["a"]
print(l)
print("Quantity:", len(l))
print()
l.append("b")
print(l)
print("Quantity:", len(l))
print()
l.extend(["c"])
print(l)
print("Quantity:", len(l))
print()
l.append(["d","e"])
print(l)
print("Quantity:", len(l))
print(l[len(l)-1])
print()
l.extend(["f","g","h"])
print(l)
print("Quantity:", len(l))
print()
