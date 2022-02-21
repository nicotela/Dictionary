sportovci = {"Nicol":[56.4, 52.8, 55.9, 50], 
             "Tomáš": [93.5, 217.4, 532.4]}
prumer_casu = {}    
for jmeno, casy in sportovci.items():
    print (f"Atlet: {jmeno}, casy: {casy}")
    prumer = sum(casy) / len(casy) 
    print (prumer)
    prumer_casu [jmeno] = prumer
print (prumer_casu)

 