def add(*args):  # konvention mit args, der * ist wichtig!
    result = 0
    for n in args:  # args ist ein tuple
        result += n
    print(result)


# nun können beliebig viele werte eingegeben werden
# add(5, 3, 2, 8, 10)

def calculate(n, **kwargs):  # kwargs = keywordarguments
    print(kwargs)  # kwargs ist ein dictionary
    # for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)  # 25

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        # get() verhindert einen Keyworderror, falls das keyword nict im dictionary enthalten ist


my_car = Car(make="Nissan")
print(my_car.model)  # gibt None aus