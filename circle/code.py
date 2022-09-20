from math import pi

default_radius = 10

def circle_perimeter(radius = default_radius): # вычисляет длину окружности
  return 2 * pi * radius

def circle_area(radius = default_radius): #  вычисляет площадь окружности
  return pi * radius ** 2 
