"""
Панграмма - предложение, которое использует каждую букву алфавита (в нашем случае - английского алфавита).
Необходимо реализовать код, который скажет, является предложение панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""


def is_sentence_is_pangram(sentence: str) -> bool:
    
    sentence = sentence.lower()
    sentence.replace(" ", "")
    alph = "abcdefghijklmnopqrstuvwxyz"
    copied_alph_from_sentence = ''
    
    for ch in sentence:
        if copied_alph_from_sentence.count(ch) == 0:
            copied_alph_from_sentence += ch

    copied_alph_from_sentence = ''.join(sorted(copied_alph_from_sentence))
    return copied_alph_from_sentence == alph
