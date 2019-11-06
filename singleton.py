# encoding: utf-8
class Singleton:
    __obj = False  # Private class variable.

    def __new__(cls,*args, **kwargs):
        if cls.__obj:
            return cls.__obj
        cls.__obj = super(Singleton, cls).__new__(cls)
        return cls.__obj
