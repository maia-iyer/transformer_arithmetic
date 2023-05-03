
from primitive_types import *
from primitive_ops import *

f = open("test.py")
lines = f.read().splitlines()

def addition(x, y):
  max_len = max(len(x), len(y))

  x = x.rjust(max_len, "0")
  y = y.rjust(max_len, "0")

  result = ''
  carry = 0

  for i in range(max_len):
    digit_one = x[-1 - i]
    digit_two = y[-1 - i]
    
    digit_sum = int(digit_one) + int(digit_two)
    digit_sum = digit_sum + carry

    cur_digit = digit_sum % 10
    carry = digit_sum // 10

    result = str(cur_digit) + result
  if carry > 0:
    result = str(carry) + result
  return result

def triple_addition(x, y, z):
  first_sum = addition(x, y)
  result = addition(first_sum, z)
  return z

def greater_than(x, y):
  max_len = max(len(x), len(y))
  x = x.rjust(max_len, "0")
  y = y.rjust(max_len, "0")

  for i in range(max_len):
    digit_one = x[i]
    digit_two = y[i]

    if int(digit_one) > int(digit_two): return '1'
    elif int(digit_one) < int(digit_two): return '0'
  return [0]
  
def sort_integers(l):
  result = []
  while len(l) > 0:
    greatest_ind = 0
    greatest_val = l[0]
    for i in range(len(l)):
      #if greater_than(l[i], greatest_val) == '1':
      if int(l[i]) > int(greatest_val):
        greatest_ind = i
        greatest_val = l[i]
    result = [greatest_val] + result
    l = l[:greatest_ind] + l[greatest_ind + 1:]
  return result

prev_vars = {}
prev_changed_var = ''
def custom_trace(frame, event, arg = None):
  global prev_vars, prev_changed_var
  #print(event, frame.f_lineno, frame.f_code, frame.f_locals)
  line_no = frame.f_lineno
  code_line = lines[line_no - 1].strip()
  local_vars = frame.f_locals
  #print(prev_vars, local_vars)
  relevant_vars = {k:v for (k,v) in local_vars.items() if k not in prev_vars or not prev_vars[k] == local_vars[k] or k == prev_changed_var}
  #print(relevant_vars)
  prev_changed_var = code_line.split("=")[0].strip()
  prev_vars = local_vars.copy()
  if len(relevant_vars) > 0:
    print(", ".join([str(k) + " = " + str(v) for (k, v) in relevant_vars.items()]))
  print(code_line)
  return custom_trace

def test_trace(l):
  import sys
  import trace

  #tracer = trace.Trace()
  #tracer.runfunc(addition, '123', '1234')

  #r = tracer.results()
  #r.write_results(show_missing=True, coverdir='.')
  sys.settrace(custom_trace)
  #ret = addition('123', '1234')
  ret = sort_integers(l)
  sys.settrace(None)
  return ret


if __name__ == '__main__':
    #FSimpleAdd = TSimpleAdd()
    #FTotalAdd = TAddition()

    #b0 = TVar(val = TInt(52))
    #b1 = TVar(val =TInt(59))
    #answer, trace = FTotalAdd.compute(b0, b1)
    #print(answer)
    #print(trace)
    l = ['4', '3', '2']
    test_trace(l)
    #pdb.set_trace()

