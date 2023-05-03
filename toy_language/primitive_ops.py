from primitive_types import *

# defining some primitive ops

# simple_add : digit x digit -> list(digit)
class TSimpleAdd(TBaseFunction):
    def __init__(self):
        super(TSimpleAdd, self).__init__("SimpleAdd")

    def compute(self, x : TVar, y : TVar, output_name = "ANSWER"):
        assert(isinstance(x.val, TDigit))
        assert(isinstance(y.val, TDigit))
        trace = f"{output_name} = {x} + {y}\n"
        answer = TInt(int(x.compute()) + int(y.compute()))
        answer, t = TSetVar().compute(output_name, answer)
        trace += t
        return answer, trace

class TRIndex(TBaseFunction):
    def __init__(self):
        super(TRIndex, self).__init__("RIndex")

    def compute(self, x : TVar, y : TVar, output_name = "ANSWER"):
        assert(isinstance(x, TVar) and isinstance(x.val, TInt))
        assert(isinstance(y, TVar) and isinstance(y.val, TInt))
        assert(x.val is not None and y.val is not None)
        trace = f"{output_name} = {x} [ {y} ]\n"
        x = x.val
        y = y.val
        len_x = len(x.val)
        if int(y.val) > len_x - 1: answer = TDigit(0)
        else: 
            index = len_x - int(y.val) - 1
            answer = TDigit(x.val[index])
        answer, t = TSetVar().compute(output_name, answer)
        trace += t
        return answer, trace

"""class TLIndex(TBaseFunction):
    def __init__(self):
        super(TLIndex, self).__init__("LIndex")

    def compute(self, x : TVar, y : TVar, output_name = "ANSWER"):
        assert(isinstance(x, TVar) and isinstance(x.val, TInt))
        assert(isinstance(y, TVar) and isinstance(y.val, TInt))
        assert(x.val is not None and y.val is not None)
        trace = f"{output_name} = {x} [ {y} ]\n"
        x = x.val
        y = y.val
        len_x = len(x.val)
        if int(y.val) > len_x - 1: answer = TDigit(0)
        else: 
            index = len_x - int(y.val) - 1
            answer = TDigit(x.val[index])
        answer, t = TSetVar().compute(output_name, answer)
        trace += t
        return answer, trace"""


class TConcat(TBaseFunction):
    def __init__(self):
        super(TConcat, self).__init__("Concat")

    def compute(self, x : TVar, y : TVar, output_name = "ANSWER"):
        assert(isinstance(x, TVar))
        assert(isinstance(y, TVar))
        trace = f"{output_name} = {x} ++ {y}\n"
        answer = TInt(int(x.val.val + y.val.val))
        answer, t = TSetVar().compute(output_name, answer)
        trace += t
        return answer, trace

class TSetVar(TBaseFunction):
    def __init__(self):
        super(TSetVar, self).__init__("SetVarFunction")

    def compute(self, var, val):
        return TVar(var, val), f"{var} = {val}\n" 

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
            digit_one, t = TRIndex().compute(x, index, "digit_one")
            trace += t
            digit_two, t = TRIndex().compute(y, index, "digit_two")
            trace += t

            digit_res, t = TSimpleAdd().compute(digit_one, digit_two, "digit_res")
            trace += t

            cur_digit, t = TRIndex().compute(digit_res, TVar(val=TInt(0)), "cur_digit")
            trace += t
            cur_digit, t = TSimpleAdd().compute(cur_digit, carry, "cur_digit")
            trace += t

            carry, t = TRIndex().compute(digit_res, TVar(val=TInt(1)), "carry")
            trace += t
            res, t = TConcat().compute(cur_digit, res, "res")
            trace += t

        res, t = TConcat().compute(carry, res, "res")
        trace += t

        res, t = TSetVar().compute(output_name, res.val)
        trace += t
            
        return res, trace

class TAddition1(TCompFunction):
    def __init__(self):
        super(TAddition1, self).__init__("TAddition1")

    def compute(self, x : TVar, y : TVar, output_name = "ANSWER"):
        assert(isinstance(x.val, TInt) and isinstance(y.val, TInt))
        max_len = max(len(x.val.val), len(y.val.val))

        res, t = TSetVar().compute("res", TInt(''))
        carry, t = TSetVar().compute("carry", TDigit(0))

        for i in range(max_len):
            index, t = TSetVar().compute('i', TInt(i))
            digit_one, t = TRIndex().compute(x, index, "digit_one")
            digit_two, t = TRIndex().compute(y, index, "digit_two")

            digit_res, t = TSimpleAdd().compute(digit_one, digit_two, "digit_res")

            cur_digit, t = TRIndex().compute(digit_res, TVar(val=TInt(0)), "cur_digit")
            cur_digit, t = TSimpleAdd().compute(cur_digit, carry, "cur_digit")

            carry, t = TRIndex().compute(digit_res, TVar(val=TInt(1)), "carry")
            res, t = TConcat().compute(cur_digit, res, "res")

        res, t = TConcat().compute(carry, res, "res")

        res, t = TSetVar().compute(output_name, res.val)
            
        return res, trace


