import numpy as np
number = np.random.randint(1, 101)

def random_predict(number:int=1) -> int:
    """_summary_ / Рандомно угадываем число

    Args:
        number (int, optional): _description_ / Загаданное число. Defaults to 1.

    Returns:
        int: _description_ / Число попыток
    """
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')