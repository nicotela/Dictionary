eshop = {"chleba":31, "houska":12, "rohlik":14}
eshop2 = [3, 1, 6, 76, 34]
"""def max (seznam):
    current_max = seznam[0]
    for hodnota in seznam:
        if hodnota > current_max:
            current_max = hodnota
    return current_max
max_eshop2 = max (eshop2)
print (max_eshop2)"""
    
for klic, hodnota in eshop.items():
    print (f"Položka {klic} stojí {hodnota} Kč.")
print ("----------------------------")

for key in eshop:
    print (f"Položka {key} stoji {eshop [key]} Kč.")
print ("----------------------------")
for value in eshop.values():
    print (f"Cena je {value} Kč.")
