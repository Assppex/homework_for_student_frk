"""
Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необзодимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> bool:
    
    words = []
    for sentence in sentences:
        sentence.count(' ')
        if len(sentence) != 0:
            words.append(sentence.count(' ') + 1)
        else:
            words.append(0)
    
        
    return max(words)
