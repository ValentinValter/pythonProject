"""NotImplementedError"""

"""Исключение, возникающее в случаях, когда наследник класса не переопределил метод, который должен был."""


class MyClass(object):

    def __init__(self):
        self.run()

    def run(self):
        raise NotImplementedError(
            'Переопределите run в %s.' % (self.__class__.__name__)
        )


class MySubclass(MyClass):
    """Наследник, у которого run должен был быть определён."""


my_obj = MySubclass()  # NotImplementedError: Определите run в MySubclass.