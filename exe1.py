from operator import index
from re import L


spends=[2200,2350,2600,2130,2190]

print ("The difference is :", spends[1]-spends[0])

print ("The total expenses fr the first three months:", spends[0]+spends[1]+spends[2])

if (any (spends) == 2000):
    print (spends)
else:
    print ("theres not such amount")
spends.append(1980)
print(spends)

spends[3] =spends[3]- 200
print (spends)