"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
    n = max(len(x), len(y))
    if n <= 4:
      return x * y
    else:
        xL, xR = split_number(x)
        yL, yR = split_number(y)
        p1 = subquadratic_multiply(xL, yL)
        p2 = subquadratic_multiply(xR, yR)
        p3 = subquadratic_multiply(xL + xR, yL + yR)
        return (p1 << (2 * (n // 2))) + ((p3 - p1 - p2) << (n // 2)) + p2
    pass

## Feel free to add your own tests here.
def test_multiply():
    x = BinaryNumber(2)
    y = BinaryNumber(2)
    res = subquadratic_multiply(x, y)
    assert res.decimal_val == x.decimal_val * y.decimal_val

    x = BinaryNumber(4)
    y = BinaryNumber(6)
    res = subquadratic_multiply(x, y)
    assert res.decimal_val == x.decimal_val * y.decimal_val

    x = BinaryNumber(90)
    y = BinaryNumber(2)
    res = subquadratic_multiply(x, y)
    assert res.decimal_val == x.decimal_val * y.decimal_val

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

test_multiply()