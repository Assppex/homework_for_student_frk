from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""
    for i in iterables:
        yield from i


class Chain:
    def __init__(self, *iterables: Iterable[T]):
        """Реализуйте класс ниже"""
        self.iterables_list = []
        
        tmp = iter(iterables)
        while True:
            try:
                ttmp = iter(next(tmp))
            except StopIteration:
                break
            
            for i in ttmp:
                self.iterables_list.append(i)
        
        self.iterables_iter = iter(self.iterables_list)
        
            
            
        # self.cur_elem_iter = iter(next(self.iter))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return next(self.iterables_iter)
        except StopIteration:
            raise


def main():
    # a = 'abcd'
    # chained = chain('abcd', 'defg')
    
    # print(list(chained))
    
    tmp = Chain('abcd', [33, 31, 32, 33])
    
    print(tmp.__next__())
    print(tmp.__next__())
    print(tmp.__next__())
    print(tmp.__next__())
    print(tmp.__next__())

if __name__ == "__main__":
    main()
    