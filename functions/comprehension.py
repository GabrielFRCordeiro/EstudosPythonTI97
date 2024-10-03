import timeit
# lista=[True,33,22,"pedro",45,67,100,97]
#
# listaNova=list()
# for valor in lista:
#     if (not isinstance(valor,bool)) and (not isinstance(valor,str)) and valor%2==0:
#         listaNova.append(valor)
#
#
# pares=[valor for valor in lista if (not isinstance(valor,bool)) and (not isinstance(valor,str)) and valor%2==0  ]
#
# print(sum(pares))
# tempo=timeit.timeit(stmt="[item for item in range(10000)]",number=1)
# tempo2=timeit.timeit(stmt="(item for item in range(10000))",number=1)
#
# print(f"Tempo em comprehension {tempo}")
# print(f"Tempo em generation {tempo2}")
# # print(listaTeste1)
# # print(listaTeste2)
listaEditavel=[item for item in range(10000)]
print(listaEditavel[34])
lista=(item for item in range(10000))
for i in lista:
    print(i)

print("-------------------")
for i in lista:
    print(i)
