from datetime import timedelta
# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])
def retry(count: int, delay : timedelta, handled_exceptions: tuple = (Exception,) ):
    if count < 1:
        raise ValueError
    def real_retry_decorator(connect_function):
        import time
        prev_err = 0
        def wrapper(*args, **kwargs):
            for retry_num in range(count - 1):
                try:
                    return connect_function(args, kwargs)
                except handled_exceptions as error:
                    prev_err = error
                    time.sleep(delay.total_seconds())
            else:
                try:
                    return connect_function(args, kwargs)
                except handled_exceptions as error:
                    raise error
        return wrapper
    return real_retry_decorator
                                    
                
# @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])----> retry не совсем декоратор (но она возвращает его), 
# поэтому пишем не @retry, а @retry(аргументы), потому что она возвращает декоратор, который декорирует некоторую
# функцию коннекта. Декоратор принимает и возвращает функцию.

                