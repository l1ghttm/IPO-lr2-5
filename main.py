import math

trapezoid_area(a, b, c, d):
   
p = (a + b + c + d) / 2

a = float(input("Введите длину основания a: "))
b = float(input("Введите длину основания b: "))
c = float(input("Введите длину боковой стороны c: "))
d = float(input("Введите длину боковой стороны d: "))

# Вычисление и вывод площади трапеции
area = trapezoid_area(p*(p - a) * (p - b) * (p - c) * (p - d)) ** 0.5
print(f"Площадь трапеции: {area}")
