import math 


   

a = float(input("Введите длину основания a: "))
b = float(input("Введите длину основания b: "))
c = float(input("Введите длину боковой стороны c: "))
d = float(input("Введите длину боковой стороны d: "))

p = (a + b + c + d) / 2

area = (p*(p - a) * (p - b) * (p - c) * (p - d)) ** 0.5
print(f"Площадь трапеции: {area}")
