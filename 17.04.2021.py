x = input('введите первое число: ')
y = input('введите второе число: ')
z = input('введите действие: ')


def kal(x, y, z):
    if x.isdigit() and y.isdigit():
        if z == '*':
            answ = int(x)*int(y)
            return answ
        if z == ':':
            answ = int(x)//int(y)
            return answ
        if z == '+':
            answ = int(x)+int(y)
            return answ
        if z == '-':
            answ = int(x)-int(y)
            return answ
    else:
        raise ValueError


try:
    kal(x, y, z)
except ValueError:
    print('вы ввели не число((')
except ArithmeticError:
    print(0)
else:
    print(kal(x, y, z))
    print('нету ошибок, молодец')
finally:
    print("щастя, здоров'я, благополуччя, успіху, гарного дня ")
