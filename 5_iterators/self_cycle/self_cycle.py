from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    storage = []
    tmp = iter(obj)
    
    for i in tmp:
        storage.append(i)
        
    while True:
        for i in storage:
            yield i
    
    


class Cycle:
    def __init__(self, obj: Iterable[T]):
        """Реализуйте класс"""
        self.storage = []
        self.current_index = 0
        for i in iter(obj):
            self.storage.append(i)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if(self.current_index <= len(self.storage) - 1):
            to_return = self.storage[self.current_index]
            self.current_index += 1
            return to_return
        else:
            self.current_index = 1
            return self.storage[0]
        


def main():
    gen = cycle('ABCD')  # Создаем генератор
    
    print(next(gen))
    
    a = Cycle('1234')
    
    for i in range(10):
        print(next(a))
    
if __name__ == "__main__":
    main()