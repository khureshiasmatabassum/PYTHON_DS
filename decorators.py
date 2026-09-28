def add(func):
    def t1():
        print("good morning")
        func()
        print("good afternoon")
    return t1


@add
def greet():
    print("hello sudha")


greet()