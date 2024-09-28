from datetime import timedelta
# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])
def retry(count: int, delay : timedelta, handled_exceptions: tuple = ()):
    if count < 1:
        raise ValueError
    def real_retry_decorator(connect_function):
        import time
        prev_err = 0
        def wrapper(*args, **kwargs):
            if len(handled_exceptions) > 0:
                for retry_num in range(count):
                    try:
                        return connect_function(args, kwargs)
                    except handled_exceptions as error:
                        prev_err = error
                    time.sleep(delay.total_seconds())
            else:
                for retry_num in range(0, count):
                    try:
                        return connect_function(args, kwargs)
                    except Exception as error:
                        prev_err = error
                    time.sleep(delay.total_seconds())
                    
            raise prev_err
        return wrapper
    return real_retry_decorator
                                    
                
# @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])----> retry не совсем декоратор (но она возвращает его), 
# поэтому пишем не @retry, а @retry(аргументы), потому что она возвращает декоратор, который декорирует некоторую
# функцию коннекта. Декоратор принимает и возвращает функцию.

                