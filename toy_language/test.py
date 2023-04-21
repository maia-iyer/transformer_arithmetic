from primitive_types import *
from primitive_ops import *
from composite_ops import *

if __name__ == '__main__':
    FSimpleAdd = TSimpleAdd()
    FTotalAdd = TAddition()

    b0 = TVar(val = TInt(52))
    b1 = TVar(val =TInt(59))
    answer, trace = FTotalAdd.compute(b0, b1)
    #print(answer)
    #print(trace)

