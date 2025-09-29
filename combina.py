# Proyecto sobre combinatoria.and


################################
## VARIACIONES SIN REPETICIÓN ##
################################
# Determina cuantos grupos de m elementos se pueden crear 
# tomando "n" elementos del total "m" sin repetir elementos.
# Por ejemplo Los grupos (1,2) y (2,1) contarían como el mismo grupo.

# Formula:
# Vm,n = m * (m-1) * (m-2)... * (m-n+1)

# m = Total de elementos
# n = Cantidad de elementos que forman los grupos buscados.


# Ejemplo:
#
# Variaciones de 2 elementoa dentro de un total de 4 elelementos.
# 
# Total de elementos: 4
# [1] [2] [3] [4]

# Tamaño de grupos formados con esos 4 elementos (Sin repeticiones)
# [1]--[2]   [2]--[1]   [3]--[1]   [4]--[1]               
# [1]--[3]   [2]--[3]   [3]--[2]   [4]--[2]  
# [1]--[4]   [2]--[4]   [3]--[3]   [4]--[3] 

# Total de elementos
m = int(input("Introduce cantidad total de elementos: "))

# Cantidad de elementos a elegir
n = int(input("Introduce cantidad de elementos que formas cada grupo: "))


def variacionesNoRep():
    resu = 1

    for i in range(n):
        resu *= m - i
    return resu

print("Existen ",variacionesNoRep(),"formas de crear grupos de",n,"elementos en de un total de",m,"sin repetir elementos.")


###############################
## VARIACIONES CON REPTICIÓN ##
###############################
# Determina cuantos grupos de m elementos se pueden crear 
# tomando "n" elementos del total "m" pudiendo repetir elementos.
# Por ejemplo Los grupos (1,2) y (2,1) contarían como grupos diferentes 
# aunque contengan los mismos elementos porque están en diferente orden.

# Formula:
# VRm,n = m^n



# Variaciones con repetición

# Permutaciones

# Permutaciones con repetición

# Combinaciones


