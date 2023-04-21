from primitive_types import *
from primitive_ops import *

class TComparison(TCompFunction):
    def __init__(self):
        super(TComparison, self).__init__("TComparison")

    

class TAddition(TCompFunction):
    def __init__(self):
        super(TAddition, self).__init__("TAddition")

    def compute(self, x : TVar, y : TVar, output_name = "ANSWER"):
        assert(isinstance(x.val, TInt) and isinstance(y.val, TInt))
        trace = f"{output_name} = {x} + {y}\n"
        max_len = max(len(x.val.val), len(y.val.val))

        res, t = TSetVar().compute("res", TInt(''))
        trace += t
        carry, t = TSetVar().compute("carry", TDigit(0))
        trace += t

        for i in range(max_len):
            index, t = TSetVar().compute('i', TInt(i))
            trace += t
            digit_one, t = TIndex().compute(x, index, "digit_one")
            trace += t
            digit_two, t = TIndex().compute(y, index, "digit_two")
            trace += t

            digit_res, t = TSimpleAdd().compute(digit_one, digit_two, "digit_res")
            trace += t

            cur_digit, t = TIndex().compute(digit_res, TVar(val=TInt(0)), "cur_digit")
            trace += t
            cur_digit, t = TSimpleAdd().compute(cur_digit, carry, "cur_digit")
            trace += t

            carry, t = TIndex().compute(digit_res, TVar(val=TInt(1)), "carry")
            trace += t
            res, t = TConcat().compute(cur_digit, res, "res")
            trace += t

        res, t = TConcat().compute(carry, res, "res")
        trace += t

        res, t = TSetVar().compute(output_name, res.val)
        trace += t
            
        return res, trace
