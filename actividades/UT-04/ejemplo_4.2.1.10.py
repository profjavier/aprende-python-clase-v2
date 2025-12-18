serie_num=[1,2,13,4,5,6,0,8,9,10]
︃mayor=serie_num[0]
menor=serie_num[0]
for i in serie_num:
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i
print(mayor,menor)