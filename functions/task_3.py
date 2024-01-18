# Задача 3 Напишите программу по следующему описанию.
# В основной ветке программы вызывается функция cylinder(), которая вычисляет
# площадь цилиндра.
# В теле cylinder определена функция circle, вычисляющая площадь круга по формуле
# πr2.
# В теле cylinder у пользователя спрашивается, хочет ли он получить только площадь
# боковой поверхности цилиндра, которая вычисляется по формуле 2πrh, или полную
# площадь цилиндра.
# В последнем случае к площади боковой поверхности цилиндра должен добавляться
# удвоенный результат вычислений функции circle().

import math

def cylinder():
    r = float(input("Введите радиус цилиндра: "))
    h = float(input("Введите высоту цилиндра: "))
    answrer = int(input("Введите: \n1 - если только S боковой\n2 - полную S цилиндра\n"))
    if answrer == 1:
        S = 2 * math.pi * r * h
        print(f"Площадь боковой поверхности цилиндра: {S:.2f}")
    elif answrer == 2:
        S = 2 * math.pi * r * h
        full_S = S + 2 * circle(r)
        print(f"Полная площадь цилиндра: {full_S:.2f}\nБоковой поверхности цилиндра: {S:.2f}")        
    
    else:
        print("Некорректный ввод. Введите '1' или '2'.")
    
def circle(r):
    S = 2*math.pi*r
    return S


cylinder()
