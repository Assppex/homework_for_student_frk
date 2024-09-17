import re

def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    text = text.lower()
    
    words = re.findall(r'\b[а-яА-Я]{3,}\b', text)
    most_common = {}
    
    for word in words:
        pattern = r'\b' + str(word) + r'\b'
        most_common[word] = len(re.findall(pattern, text))
    
    
    # print(most_common.items())
    
    most_common = dict(sorted(
        most_common.items(),
        key = lambda x: (-x[1],x[0]),
        #reverse=True -x[1] - по значению идем по убыванию (приоритетный признак), x[0]-в случае равенства идем по возрастанию в алфавитном порядке (т.е. нам надо чтобы в случае возникновения твбг = x и чеёж = x ---> {'твбг':x, 'чеёж':x}), в случае если проставить reverse = True будет наоборот, потому что reverse применится к обеим сортировкам
        )[0:10])

    print(most_common)
    
    return most_common
