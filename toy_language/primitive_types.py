class TLanguageError(Exception):
    pass

class TOutOfBoundsError(TLanguageError):
    pass

# TODO : val can be set arbitrarily and break
class TDigit:
    def __init__(self, val):
        if int(val) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            raise TLanguageError("invalid TDigit instantiated")
        self.val = str(val)

    def __repr__(self):
        return self.val

    def compute(self):
        return self.val

class TInt:
    def __init__(self, val):
        if isinstance(val, int) and val >= 0:
            self.val = str(val)
        elif isinstance(val, str):
            assert(len(val) == 0)
            self.val = ''
            
    def __repr__(self):
        return " ".join(self.val)

    def is_digit(self):
        return len(self.val) == 1

    def to_digit(self):
        assert(len(self.val) == 1)
        return TDigit(self.val)

    def compute(self):
        return self.val

class TVar:
    def __init__(self, name = None, val=None):
        self.name = name if name is not None else str(val)
        assert(type(val) in [TInt, TDigit, TBool, TLanguageError])
        self.val = val

    def __repr__(self):
        return str(self.name)

    def compute(self):
        return self.val.val

class TFunction:
    def __init__(self, name):
        self.name = name

    # return answer + trace
    def compute(self, *args):
        raise NotImplementedError

# TODO delete the following probably
class TBaseFunction(TFunction):
    def __init__(self, name):
        self.name = name

class TCompFunction(TFunction):
    def __init__(self, name):
        self.name = name
