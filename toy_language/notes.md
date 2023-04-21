# primitive objects

boolean
digit
list of digit + ()
variable
function
tuple


conditional
loop

# primitive ops

```
simple_add : digit x digit -> list(digit)
simple_less_than : digit x digit -> boolean
simple_equality : digit x digit -> boolean

list_len : list(digit) -> list(digit)
cons_head : list(digit) -> digit x list(digit)
```

-----

# pseudocode

```python
class ToyFunction:
  def init():
    self.name = ""

    # input type should be based on the primitive objects, but not variable or function probably
    self.input_type = ""
    self.list_of_ops = []
  def trace_computation(input):
  def sparsify_computation(computation)
```
