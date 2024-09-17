import numpy as np
def decode_numbers(numbers: str) -> str | None:
    letters = np.array([['а', 'б', 'в', 'г'], ['д', 'е', 'ж', 'з'], ['и', 'й', 'к', 'л'], ['м','н','о','п'], ['р','с','т','у'], ['ф','х','ц','ч'], ['ш','щ','ъ','ы'], ['ь','э','ю','я']])
    special_symbols = np.array(['.', ',', '?', '!', ':', ';'])
    """Пишите ваш код здесь."""
    result = ""
    splitted_nums = numbers.split(' ')
    
    for letter in splitted_nums:
        if(letter.count(letter[0]) == len(letter)):
            if int(letter[0]) - 2 >= 0 and  len(letter) <= 4:
                result += letters[int(letter[0]) - 2][len(letter) - 1]
            elif int(letter[0]) == 1 and  len(letter) <= 6:
                result += special_symbols[len(letter) - 1]
            elif int(letter[0]) == 0 and len(letter) == 1:
                result += ' '
            else:
                return None
        else:
            return None
        print(result)
            
            
    return result