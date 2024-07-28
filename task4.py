import numpy as np

# Исходный код
numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
    squares.append(number**2)


# Использование list comprehension для повышения производительности
squares = [number**2 for number in range(1, 1000001)]

# Использование numpy для большего повышения скорости
numbers = np.arange(1, 1000001)
squares = numbers**2
