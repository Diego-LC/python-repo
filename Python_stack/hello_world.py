print ("hola mundo")

mi_nombre = 'Diego'
print ("Mi nombre es", mi_nombre)
print ("Mi nombre es " + mi_nombre)
print ("Mi nombre es %s" % mi_nombre)
print ("Mi nombre es {}".format(mi_nombre))
print (f"Mi nombre es {mi_nombre}")

num = 8
print ("Hola!",num)
print ("Hola %d!"%num)

food1 = 'pizzas'
food2 = 'helados'
print (f'Me encanta comer {food1} y {food2}')
print ("Me encanta comer {} y {}".format(food1,food2))
print ("Me encanta comer %s y %s" % (food1,food2))

cadena = "Me encanta comer %s y %s" % (food1.upper(),food2)
print (cadena)
list = cadena.split()
print (list)
# list = list.join()
# print(list)
