import numpy as np
def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""
    result = ""
    # Получим таблицу кодировки из букв в клавиши телефона без ручного ввода
    
    letters = np.array([['а', 'б', 'в', 'г'], ['д', 'е', 'ж', 'з'], ['и', 'й', 'к', 'л'], ['м','н','о','п'], ['р','с','т','у'], ['ф','х','ц','ч'], ['ш','щ','ъ','ы'], ['ь','э','ю','я']])
    special_symbols = np.array(['.', ',', '?', '!', ':', ';'])
    
    letters_table_encode = {}
    
    for i in range(0,8):
        for j in range(0,4):
            letters_table_encode[str(letters[i][j])] = (j+1)*str(i+2)
            
    for i in range(0,len(special_symbols)):
        letters_table_encode[str(special_symbols[i])] = (i+1)*'1'

    letters_table_encode[' '] = '0' #Таблица кодировки получена
    # print(letters_table_encode)
            
    for symb in text:
        # print(symb)
        try:
            result += letters_table_encode[symb]
            result += ' '
        except KeyError:
            return None
    result = result[0:len(result) - 1] #Убираем лишний пробел в конце
    return result
