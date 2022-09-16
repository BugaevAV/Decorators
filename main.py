import datetime
import os

# Задание 1
def logger(any_function):

    def dec_function(*args, **kwargs):
        result = any_function(*args, **kwargs)
        with open('logger.txt', 'a', encoding='utf-8') as file:
            log = file.write(f'{datetime.datetime.now().strftime("%H:%M %d.%m.%Y")},'
                             f' функция {any_function.__name__} с аргументами {args} {kwargs}\n'
                             f' вернула {result}\n')
    return dec_function

@logger
def file_path(file_name):
    return os.path.abspath(file_name)


# Задание 2
def logger_path(path):
    def logger(any_function):
        def decor_function(*args, **kwargs):
            result = any_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                log = file.write(f'{datetime.datetime.now().strftime("%H:%M %d.%m.%Y")},'
                                 f' функция {any_function.__name__} с аргументами {args} {kwargs}\n'
                                 f' вернула {result}\n')
                return result
        return decor_function
    return logger


@logger_path('logger.txt')
def div(a, b):
    return round(a / b, 1)


if __name__ == '__main__':
    file_path('logger.txt')
    div(2, 3)

