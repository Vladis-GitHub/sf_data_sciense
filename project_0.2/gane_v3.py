""" ИГРА УГАДАЙ ЧИСЛО 
    Компьютер сам загадывает и сам угадывает число (методом Дихотомии)
"""

import numpy as np

def predict(number: int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Количество попыток
    left_pt = 1 # левый конец отрезка поиска числа
    right_pt = 100+1 # правый конец отрезка поиска числа 
                     # (прибавление 1(ед.) - способ избежать зацикливания, когда number=100, а 
                     # predict_number менятется посредством операциии "...//2"; 
                     # если же predict_number менять посредством "round(.../2)", 
                     # то зацикливание возможно, когда number=1, и для его избежания можно положить 
                     # left_pt = 0)

    while True:
        count += 1
        predict_number = (left_pt + right_pt) // 2 # предполагаемое число
        if predict_number == number:
            break
        elif predict_number > number:
            right_pt = predict_number
        else:
            left_pt = predict_number
    return(count)


def score_game(predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов происхрдит угадывание

    Args:
        predict (_type_): функция угадывания

    Returns:
        int: среднее количесво попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости...
    random_array = np.random.randint(1, 101, size=(1000)) # генерация 1000 псевдослучайных чисел, 
                                                          # от 1 до 100 каждое
    
    for number in random_array:
        count_ls.append(predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return(score)

score_game(predict)