"""Реализуйте необходимые функции ниже."""

def zero(operation = None):
    if operation:
        return operation(0)
    else:
        return 0
    
def one(operation = None):
    if operation:
        return operation(1)
    else:
        return 1

def two(operation = None):
    if operation:
        return operation(2)
    else:
        return 2


def three(operation = None):
    if operation:
        return operation(3)
    else:
        return 3  


def four(operation = None):
    if operation:
        return operation(4)
    else:
        return 4  

def five(operation = None):
    if operation:
        return operation(5)
    else:
        return 5  

def six(operation = None):
    if operation:
        return operation(6)
    else:
        return 6  


def seven(operation = None):
    if operation:
        return operation(7)
    else:
        return 7

def eight(operation = None):
    if operation:
        return operation(8)
    else:
        return 8


def nine(operation = None):
    if operation:
        return operation(9)
    else:
        return 9

# Функции zero, one, two итд - это не замыкания, поскольку они не замыкают переменные из внешней оболочки (не сохраняют состояние), они сразу возвращают некоторое значение (т.к. operation - это вообще говоря функция (см ниже)), а вот plus, minus итд - это замыкания: они возвращают внутренню функцию как обьект,
# а не значение результат работы внутренней функции, т.е.они замыкают operand - второй операнд выражения и ждут x - первый операнд, в функциях one , two итд мы как раз на вход подаем им первый операнд 1, 2 итд и сразу требуем от них результата ---> вызываем operation(x), а это обычная функция, она возвращает число
# plus(x) ---> вернет обьект (функцию) action которая как раз будет ждать первый опреанд, храня второй - замыкание 


def plus(operand):
    def action(x):
        return x + operand
    return action

def minus(operand):
    def action(x):
        return x - operand
    return action

def divided_by(operand):
    def action(x):
        try:
            return x // operand
        except ZeroDivisionError:
            print("Деление на ноль")
            exit(-1)
    return action

def times(operand):
    def action(x):
        return x * operand #тут не operand() потому что в функции действий передается что-то вроде: one() ---> обычный int, не функция
    return action #возвращаем внтуреннюю функцию, но не результат ее работы

    
def main():
    print(one(divided_by(zero())))
    
if __name__ == "__main__":
    main()

# def two():
    
# def three():
    
# def four():
    
# def five():
    
# def six():
    
# def seven():
    
# def eight():
    
# def nine():
    
    
    
# def plus(opernad_second):
#     def inside():
#         return oprand_first() + opernad_second()
        

# def minus():
#     operation = '-'

# def times():
#     operation = '*'
    
# def divided_by():
#     operation = '/'    
    