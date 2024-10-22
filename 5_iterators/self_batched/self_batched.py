from typing import Generator, Iterable, TypeVar
# from itertools import batched

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Пиши свой код здесь."""
    if n < 1:
        raise ValueError
    entity_size = len(obj)
    iterator = iter(obj)
    
    while entity_size > 0:
        if(entity_size // n > 0):
            yield [next(iterator) for i in range(n)]
            entity_size = entity_size - n
        else:
            yield [next(iterator) for i in range(entity_size)]
            entity_size = 0
            
#Генератор в еденицу времени думает только об одном обьекте, о том, который возвращает (yield), когда он его вернет, мы начинаем строить новый кортеж, о старом уе забыли. next(iterator) работает таким оразом, что next меняет сам итератор на следующий обьект


class Batched:
    """Реализуй этот класс."""
    def __init__(self, obj: Iterable[T], n: int):
        if n < 1:
            raise ValueError
        self.obj = iter(obj)
        self.n = n
        self.entity_size = len(obj)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # if(self.entity_size > 0):
        if(self.entity_size // self.n > 0):
            self.entity_size = self.entity_size - self.n
            return [next(self.obj) for i in range(self.n)]
        else:
            return [next(self.obj) for i in range(self.entity_size)]
        
        
# for i in batched_iter как бы каждый раз происходит нечто: i = batched_iter.__next()__
        
def main():
    # a = 'abcdef'
    
    # for batch in batched('ABCDEFG', 3):
    #     print(batch)
    
    batched_iter = Batched('ABCDEFG', 3)

    # for batch in batched_iter:
    #     print(batch)
    
if __name__ == "__main__":
    main()