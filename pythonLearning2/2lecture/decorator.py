from datetime import datetime
import time


def decorator(fn):
    def wrapper(*args):
        print("Run function: " + str(fn.__name__) + "() with param" + str(args))
        start = datetime.now()
        fn(*args)
        time.sleep(2)
        end = datetime.now()
        print("время выполнения: " + str(end - start))

        if args[0] > 1000:
            print("Параметр должен быть меньше 1000")
    return wrapper

@decorator
def sum(a,b):
    return a + b

c = sum(1500,5)