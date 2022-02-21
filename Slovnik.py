d = {"rohlik":5, "chleba":20}
d["houska"] = 6
print (d)
d["rohlik"] = 12
print (d)
del d["rohlik"]
print (d)
d.pop("houska")
print (d)
print (d["chleba"])
print ("chleba" in d)
print ("sadc" in d) #použít u podmínky příp. 

print (d.get("chlefba", 0))