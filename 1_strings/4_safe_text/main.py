import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    
    wrong_article = get_wrong_article()
    wrong_article = wrong_article.replace("!","")
    wrong_article = wrong_article.lower()
    
    reversed_article = ''
    index_of_str_start = -1
    wrong_article = wrong_article.replace('foow-foow','tac')
        
    for i in range(0, len(wrong_article)):
        if wrong_article[i] == '\n':
            for j in range(i-2, index_of_str_start, -1):
                if wrong_article[j] != '.':
                        if j == i-2:
                            reversed_article += wrong_article[j].upper()
                            print(reversed_article)
                        else:
                            reversed_article += wrong_article[j]
            index_of_str_start = i
            reversed_article += '.\n'
            
    
    wrong_article = reversed_article

    # Ваш код ниже, возвращайте уже отредактированный текст!
    return wrong_article
