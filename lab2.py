# РЕШЕНИЕ ДУ МЕТОДОМ ЭЙЛЕРА, КОШИ И ТЕЙЛОРА 2 ПОРЯДКА

import matplotlib.pyplot as plt
from math import e
import numpy as np

# Аналитически найденное решение ДУ:
def y(x):
    return 0.1 * e ** ( (50 / 3) * (x ** 3) \
                     - (145 / 4) * (x ** 2) \
                      + (51 / 2) *  x)

# Правая часть уравнения:
def f(x, y):
    return 50 * y * (x - 0.6) * (x - 0.85)

# 1-ая производная f по x:   
def df_dx(x, y):
    return 50 * (f(x, y) * (x - 0.6) * (x - 0.85) \
                 + y * (2 * x - 1.45))

# 2-ая производная f по x:
def df_dx_2(x, y):
    return 50 * (df_dx(x, y) * (x - 0.6) * (x - 0.85) \
                 + 2 * f(x, y) * (2 * x - 1.45) + 2 * y)

# 3-я производная f по x:
def df_dx_3(x, y):
    return 50 * (df_dx_2(x,y) * (x - 0.6) * (x - 0.85) \
                 + 3 * df_dx(x, y) * (2 * x - 1.45) + 6 * f(x, y))

                      
# Вычисление приближенного решения ДУ тремя методами (Эйлера, Коши и Тейлора 4 порядка): 
def calculate():

    # Массив значений на оси x для вывода графика функции y (точного решения ДУ): 
    rr = np.arange(0, 1, 0.0001)
    
    while True:
        try:
            N = int(input("Please input natural number N: "))
            if N <= 1: raise ValueError
        except ValueError:
            # Сообщение об ошибке, если N не число или не натуральное число, или вещественное число:
            print("Oops!  That was no valid number.  Try again...")
        else:
        
            # h - шаг методов. h1, h2, h3 - необходимы для метода Тейлора 4 порядка
            h = 1 / (N - 1)
            h1 = (h ** 2) / 2 
            h2 = (h ** 3) / 6
            h3 = (h ** 4) / 24
            
            # Инициализируем начальное значение x
            x = 0
            
            # Инициализируем значения y(x0) для всех трёх методов
            y_E = y(0)
            y_C = y(0)
            y_T = y(0)
            
            # Инициализируем массивы, куда будем аккумулировать значения x_k и y_k для всех трёх методов
            X = [0]
            Y_E = [y_E]
            Y_C = [y_C]
            Y_T = [y_T]
            
            # Делаем пересчет значений x и y по реккурентным формулам
            for i in range(N - 1):
                y_E += h * f(x,y_E)
                y_C += h * f(x + h / 2, y_C + (h / 2) * f(x, y_C))
                y_T += h * f(x,y_T) + \
                       h1 * df_dx(x,y_T) + \
                       h2 * df_dx_2(x,y_T) + \
                       h3 * df_dx_3(x,y_T) 
                x += h
                
                # Добавляем следующие значения в соответствующие массивы значений x_k и y_k
                X.append(x)
                Y_E.append(y_E)
                Y_C.append(y_C)
                Y_T.append(y_T)
                
            # Для более приятной картинки, убираем точки узлов с графика, если N > 91. Иначе, получается некрасиво
            if N >= 91: 
                Marker = ''
            else: Marker = '.'
            
            # Cоздаем графики для всех методов и для точного решения
            plt.plot(X, Y_E, color='#F01F1F', linestyle='--', marker=Marker, label='Метод Эйлера')
            plt.plot(X, Y_C, color='#2EBA45', linestyle='--', marker=Marker, label='Метод Коши')
            plt.plot(X, Y_T, color='#01FFCD', linestyle='--', marker=Marker, label='Метод Тейлора 4 порядка')
            plt.plot(rr, y(rr), label='Точное решение')
            
            # Создаем название для графика
            plt.title("Сравнение численных методов решения начальной задачи Коши")
            
            # Даем имена осям
            plt.xlabel("ось x")
            plt.ylabel("ось y")
            
            # Используем этот метод для удаления лишнего белого/пустого пространства
            plt.tight_layout()
            
            # Стиль графика:
            plt.style.use('fast')
            
            # Добавляем сетку на график, чтоб было удобнее его анализировать
            plt.grid()
            
            # Добавляем легенду
            plt.legend()
            
            # Показываем график
            plt.show()

calculate()

input()
