# making list comprehensions
serie_1 = range(100)
serie_2 = range(100)

result=[(x+y) for x,y in zip(serie_1 , serie_2)]
print(result)