import os
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    _ = get_employees_info()
    print(_)
    parsed_employees_info = []
    # Ваш код ниже
    pass_list = ['id', 'name', 'last_name', 'age', 'salary', 'position']
    
    for el in _:
        list_el = el.split()
        tmp_dict = {}
        for i in range(0, len(list_el)):
            # print(pass_list.count(list_el[i]))
            if i % 2 == 0 and pass_list.count(list_el[i]) != 0:
                if list_el[i] == 'age' or list_el[i] == 'id':
                    tmp_dict[list_el[i]] =  int(list_el[i + 1])
                elif list_el[i] == 'salary':
                    tmp_dict[list_el[i]] = Decimal(list_el[i + 1])
                else:
                    tmp_dict[list_el[i]] = list_el[i + 1]
        print(tmp_dict)
        parsed_employees_info.append(tmp_dict)
                
    return parsed_employees_info

def main():
    get_parsed_employees_info()
    
if __name__ == "__main__":
    main()
    