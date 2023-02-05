# Write an algorithm to count the number of capital letters in a string. 
# How many comparisons does it do? What is the fewest number of increments it might do? What is the largest number? 
# (use N for the number of characters in the string).

def count_capital_letters(string):
    count = 0
    for letter in string:
        if letter.isupper():
            count += 1
    return count

#Respuesta: El alogritmo realiza N comparaciones donde N es el número de carctéres de la cadena.
# El número mínimo de incrementos es 0 y el máximo es N.



# Without using compound conditional expressions, write an algorithm that takes in three integers and determines if they are all distinct. On average, how many comparisons does your algorithm do? Remember to examine all input classes.

def distinct(x,y,z):
    if x == y:
        return False
    if x == z:
        return False
    if y == z:
        return False
    return True

#Respuesta: El algoritmo realiza 3 comparaciones en el peor de los casos. En el mejor de los casos realiza 1 comparación.


# Write an algorithm that takes in three distinct integers and determines the largest of three. What are the possible input classes that would have to be considered when analyzing this algorithm? Which one causes your algorithm to do the most comparisons? Which one the least? (if there is no difference between the most and the least, rewrite the algorithm with simple conditionals and without using temporary variables so that the best case gets faster than the worst one).

def largest(x,y,z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > x and z > y:
        return z
    if x == y and x > z:
        return x
    if x == z and x > y:
        return x
    if y == z and y > x:
        return y
    return x

#Respuesta: El algoritmo realiza 12 comparaciones en el peor de los casos. En el mejor de los casos realiza 2 comparaciones. Los casos de entrada que hacen que el algoritmo realice más comparaciones son cuando los tres números son iguales, cuando dos números son iguales y cuando todos los números son distintos. Los casos de entrada que hacen que el algoritmo realice menos comparaciones son cuando se introduce el número mayor de primero y los otros dos son diferentes.


# Write an algorithm to find the second largest element in a list of N values. How many comparisons does your algorithm do in the worst case? 

def second_largest(v):
    v.sort()
    return v[-2]
# hola = [1,2,44,44,6,3,9]


def larguest_2(v):
    m = 0
    sm = 0
    for i in v:
        if i > m:
            sm = m
            m = i
        elif i > sm:
            sm = i
    return sm

#Respuesta: El algoritmo realiza N comparaciones en el peor de los casos. En el mejor de los casos realiza 1 comparación.


# Write an algorithm that finds the middle, or median, value of three distinct integers. What is the best case of your algorithm? What is the worst case? What is the average case?


def median(x,y,z):
    if x > y and x < z:
        return x
    if x < y and x > z:
        return x
    if y > x and y < z:
        return y
    if y < x and y > z:
        return y
    if z > x and z < y:
        return z
    if z < x and z > y:
        return z
    return x

#Respuesta: El algoritmo realiza 6 comparaciones en el peor de los casos. En el mejor de los casos realiza 1 comparación. El caso promedio es de 3 comparaciones.


# Write an algorithm that determines if four integers are distinct. What is the best case for your algorithm? What is the worst case? What is the average case? 

def distinct_4(x,y,z,w):
    if x == y or x == z or x == w:
        return False
    if y == z or y == w:
        return False
    if z == w:
        return False
    return True

#Respuesta: El algoritmo realiza 6 comparaciones en el peor de los casos. En el mejor de los casos realiza x comparaciones. El caso promedio es de 3 comparaciones.
