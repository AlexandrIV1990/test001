from datetime import datetime

def timeit(arg):
    def function(func):
        def decor(*args, **kwargs):
            start=datetime.now()
            result=func(*args, **kwargs)
            print(arg + ": " + str(datetime.now()-start))
            return result
        return decor
    return function


@timeit("итоговое время")
def begin(n):
    spisok=[]
    for i in range(n):
        if i%3==0:
            spisok.append(i)
    return spisok


begin(900000)