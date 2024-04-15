from io import StringIO
import unittest
from unittest.mock import patch





def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):

        if isinstance((a,b), int):
            raise TypeError("values must be an integer")
        if a or b < 0:
            raise TabError("values must be a positive inter=ger")
        if a < b:
            a,b = b,a
            return func(a,b)
        print(a/b)
    return inner

div1 = smart_div(div)

div1(2,4)



