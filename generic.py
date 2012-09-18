class Generic(object):
    """Stores attributes in a Generic class.

    example usage:
    |> a = 6
    |> b = 8
    |> c = 13.5
    |> import generic
    |> params = generic.Generic(a=a, b=b, c=c)
    |> params
       <generic.Generic object at 0x0536EDD0>
    |> params.a
       6
    |> params.b
       8
    |> params.c
       13.5
    |> params.__dict__
       {'a': 6, 'b': 8, 'c': 13.5}

    """
    
    def __init__(self, **kw):
        self.__dict__ = kw